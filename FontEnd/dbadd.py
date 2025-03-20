import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# MySQL conn data
MYSQL_HOST = ""
MYSQL_USER = ""
MYSQL_PW = ""
MYSQL_DB_NAME = ""

# Function to connect to database
def connect_db():
    return mysql.connector.connect(
        host = MYSQL_HOST,  
        user = MYSQL_USER,
        password = MYSQL_PW,  
        database = MYSQL_DB_NAME,
    )

# API Route to Insert AI Data
@app.route('/add_ai', methods=['POST'])
def add_ai():
    data = request.json  # Receive JSON data from frontend
    name = data.get("name")
    link = data.get("link")
    price = data.get("price")
    rating = data.get("rating")

    if not all([name, link, price, rating]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = connect_db()
        cursor = conn.cursor()
        sql_query = "INSERT INTO ai (name, link, price, rating) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql_query, (name, link, price, rating))
        conn.commit()
        conn.close()
        return jsonify({"message": "AI added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the server

