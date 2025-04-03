from flask import Flask, request, jsonify, render_template, redirect
import mysql.connector
from flask_cors import CORS

app = Flask(__name__, template_folder="template")
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="searchai_maindb"
    )

# ========== HTML ROUTES ==========

@app.route("/")
def user():
    return render_template("User.html")

@app.route("/Admin")
def admin():
    return render_template("Admin.html")

# ========== ADD AI ==========

@app.route("/add-ai", methods=["POST"])
def add_ai():
    data = request.get_json()

    name = data.get("name")
    link = data.get("link")
    description = data.get("description")
    type_ = data.get("type")
    price = data.get("price")
    price_description = data.get("priceDescription")
    rating = int(data.get("ranking"))
    target_group = data.get("targetGroup")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Add to AI table
        cursor.execute("INSERT INTO ai (name, link, price, rating) VALUES (%s, %s, %s, %s)", (name, link, price, rating))
        ai_id = cursor.lastrowid

        # Description
        cursor.execute("INSERT INTO description (name) VALUES (%s)", (description,))
        description_id = cursor.lastrowid
        cursor.execute("INSERT INTO ai_has_description (ai_id, description_id) VALUES (%s, %s)", (ai_id, description_id))

        # Type
        cursor.execute("SELECT id FROM type WHERE name = %s", (type_,))
        type_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO ai_has_type (ai_id, type_id) VALUES (%s, %s)", (ai_id, type_id))

        # Pricing Model
        cursor.execute("SELECT id FROM pricingmodel WHERE name = %s", (price,))
        pricing_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO ai_has_pricingmodel (ai_id, pricingmodel_id) VALUES (%s, %s)", (ai_id, pricing_id))

        # Target Group
        cursor.execute("SELECT id FROM targetgroup WHERE name = %s", (target_group,))
        target_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO ai_has_targetgroup (ai_id, targetgroup_id) VALUES (%s, %s)", (ai_id, target_id))

        conn.commit()
        return jsonify({"message": "KI erfolgreich hinzugefügt!"})

    except mysql.connector.Error as err:
        print("Fehler:", err)
        return jsonify({"message": f"Fehler beim Hinzufügen: {err}"}), 500

    finally:
        cursor.close()
        conn.close()

# ========== GET AIs (USER MODE) ==========

@app.route("/get-ais", methods=["POST"])
def get_ais():
    filters = request.json
    name = filters.get("name", "")
    price = filters.get("price", "")
    ranking = filters.get("ranking", "")
    targetgroup = filters.get("targetGroup", "")

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT ai.name, ai.link, ai.price, ai.rating
        FROM ai
        LEFT JOIN ai_has_targetgroup ON ai.id = ai_has_targetgroup.ai_id
        LEFT JOIN targetgroup ON ai_has_targetgroup.targetgroup_id = targetgroup.id
        WHERE 1=1
        """
        params = []

        if name:
            query += " AND ai.name LIKE %s"
            params.append(name + "%")

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

        return jsonify(result)

    except mysql.connector.Error as err:
        print("Fehler:", err)
        return jsonify({"message": f"Fehler beim Abrufen: {err}"}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True, port=5500)
