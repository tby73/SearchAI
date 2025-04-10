from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import mysql.connector
from flask_cors import CORS
from mysql.connector import Error
import os

app = Flask(__name__, 
             template_folder="template",
             static_folder="static", 
             static_url_path='/static')
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5500", "http://127.0.0.1:5500"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Database configuration
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="searchai_maindb"
    )

# ========== HTML ROUTES ==========

@app.route("/")
def home():
    return render_template("User.html")

@app.route("/admin")
def admin_mode():
    return render_template("Admin.html")

@app.route("/user")
def user_mode():
    return render_template("User.html")

# ========== ADD AI (Admin mode) ==========

@app.route("/add-ai", methods=["POST"])
def add_ai():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug print
        
        if not data:
            return jsonify({"message": "No data received"}), 400

        name = data.get("name")
        link = data.get("link")
        description = data.get("description")
        type_ = data.get("type")
        price = data.get("price")
        price_description = data.get("priceDescription")
        ranking = data.get("ranking")
        target_group = data.get("targetGroup")

        print("Parsed values:", {  # Debug print
            "name": name,
            "link": link,
            "description": description,
            "type": type_,
            "price": price,
            "price_description": price_description,
            "ranking": ranking,
            "target_group": target_group
        })

        # Validate required fields
        if not all([name, link, description, type_, price, ranking, target_group]):
            missing_fields = [field for field, value in {
                "name": name,
                "link": link,
                "description": description,
                "type": type_,
                "price": price,
                "ranking": ranking,
                "target_group": target_group
            }.items() if not value]
            return jsonify({"message": f"Missing fields: {', '.join(missing_fields)}"}), 400

        try:
            rating = int(ranking)
        except (ValueError, TypeError):
            return jsonify({"message": "Invalid ranking value"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Start transaction
            conn.start_transaction()

            # Add to AI table
            cursor.execute("INSERT INTO ai (name, link, price, rating) VALUES (%s, %s, %s, %s)", 
                         (name, link, price, rating))
            ai_id = cursor.lastrowid

            # Description
            cursor.execute("INSERT INTO description (name) VALUES (%s)", (description,))
            description_id = cursor.lastrowid
            cursor.execute("INSERT INTO ai_has_description (ai_id, description_id) VALUES (%s, %s)", 
                         (ai_id, description_id))

            # Type - Insert if not exists
            cursor.execute("INSERT IGNORE INTO type (name) VALUES (%s)", (type_,))
            cursor.execute("SELECT id FROM type WHERE name = %s", (type_,))
            type_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO ai_has_type (ai_id, type_id) VALUES (%s, %s)", 
                         (ai_id, type_id))

            # Pricing Model - Insert if not exists
            cursor.execute("INSERT IGNORE INTO pricingmodel (name) VALUES (%s)", (price,))
            cursor.execute("SELECT id FROM pricingmodel WHERE name = %s", (price,))
            pricing_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO ai_has_pricingmodel (ai_id, pricingmodel_id) VALUES (%s, %s)", 
                         (ai_id, pricing_id))

            # Target Group - Insert if not exists
            cursor.execute("INSERT IGNORE INTO targetgroup (name) VALUES (%s)", (target_group,))
            cursor.execute("SELECT id FROM targetgroup WHERE name = %s", (target_group,))
            target_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO ai_has_targetgroup (ai_id, targetgroup_id) VALUES (%s, %s)", 
                         (ai_id, target_id))

            # Commit transaction
            conn.commit()
            return jsonify({"success": True, "message": "AI successfully added!"})

        except mysql.connector.Error as err:
            # Rollback transaction on error
            conn.rollback()
            print("Database Error:", err)
            return jsonify({"success": False, "message": f"Error adding AI: {err}"}), 500
        finally:
            cursor.close()
            conn.close()

    except Exception as e:
        print("General Error:", e)
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500

# ========== GET AIs (User mode) ==========

@app.route("/get-ais", methods=["POST"])
def get_ais():
    try:
        filters = request.json or {}
        name = filters.get("name", "")
        price = filters.get("price", "")
        ranking = filters.get("ranking", "")
        targetgroup = filters.get("targetGroup", "")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT ai.id, ai.name, ai.link, ai.price, ai.rating, description.name as description,
               type.name as type, targetgroup.name as target_group
        FROM ai
        LEFT JOIN ai_has_description ON ai.id = ai_has_description.ai_id
        LEFT JOIN description ON ai_has_description.description_id = description.id
        LEFT JOIN ai_has_type ON ai.id = ai_has_type.ai_id
        LEFT JOIN type ON ai_has_type.type_id = type.id
        LEFT JOIN ai_has_targetgroup ON ai.id = ai_has_targetgroup.ai_id
        LEFT JOIN targetgroup ON ai_has_targetgroup.targetgroup_id = targetgroup.id
        WHERE 1=1
        """
        params = []

        if name:
            query += " AND ai.name LIKE %s"
            params.append(f"%{name}%")

        if price:
            query += " AND ai.price = %s"
            params.append(price)

        if ranking:
            query += " AND ai.rating >= %s"
            params.append(int(ranking))

        if targetgroup:
            query += " AND targetgroup.name = %s"
            params.append(targetgroup)

        query += " ORDER BY ai.rating DESC"

        cursor.execute(query, params)
        result = cursor.fetchall()
        
        return jsonify({"success": True, "ais": result})

    except mysql.connector.Error as err:
        print("Error:", err)
        return jsonify({"success": False, "message": f"Error retrieving data: {err}"}), 500
    except Exception as e:
        print("General Error:", e)
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# Create database tables if they don't exist
def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create ai table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            link VARCHAR(255) NOT NULL,
            price VARCHAR(100) NOT NULL,
            rating INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create description table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS description (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
        
        # Create ai_has_description table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_has_description (
            ai_id INT NOT NULL,
            description_id INT NOT NULL,
            PRIMARY KEY (ai_id, description_id),
            FOREIGN KEY (ai_id) REFERENCES ai(id) ON DELETE CASCADE,
            FOREIGN KEY (description_id) REFERENCES description(id) ON DELETE CASCADE
        )
        """)
        
        # Create type table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS type (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            UNIQUE KEY (name)
        )
        """)
        
        # Create ai_has_type table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_has_type (
            ai_id INT NOT NULL,
            type_id INT NOT NULL,
            PRIMARY KEY (ai_id, type_id),
            FOREIGN KEY (ai_id) REFERENCES ai(id) ON DELETE CASCADE,
            FOREIGN KEY (type_id) REFERENCES type(id) ON DELETE CASCADE
        )
        """)
        
        # Create pricingmodel table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pricingmodel (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            UNIQUE KEY (name)
        )
        """)
        
        # Create ai_has_pricingmodel table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_has_pricingmodel (
            ai_id INT NOT NULL,
            pricingmodel_id INT NOT NULL,
            PRIMARY KEY (ai_id, pricingmodel_id),
            FOREIGN KEY (ai_id) REFERENCES ai(id) ON DELETE CASCADE,
            FOREIGN KEY (pricingmodel_id) REFERENCES pricingmodel(id) ON DELETE CASCADE
        )
        """)
        
        # Create targetgroup table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS targetgroup (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            UNIQUE KEY (name)
        )
        """)
        
        # Create ai_has_targetgroup table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_has_targetgroup (
            ai_id INT NOT NULL,
            targetgroup_id INT NOT NULL,
            PRIMARY KEY (ai_id, targetgroup_id),
            FOREIGN KEY (ai_id) REFERENCES ai(id) ON DELETE CASCADE,
            FOREIGN KEY (targetgroup_id) REFERENCES targetgroup(id) ON DELETE CASCADE
        )
        """)
        
        conn.commit()
        print("Database tables created successfully")
        
    except mysql.connector.Error as err:
        print(f"Error creating database tables: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    init_db()  # Create tables if they don't exist
    app.run(debug=True, port=5500)
