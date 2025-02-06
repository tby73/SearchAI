import mysql.connector
import json
from flask import jsonify

def check_login(email, password):
    try:
        # Verbindung zur Datenbank herstellen
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="p2c-data"
        )
        cursor = conn.cursor(dictionary=True)

        # SQL-Abfrage um Benutzer zu finden
        sql = "SELECT * FROM userinformations WHERE email = %s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        # Verbindung schließen
        cursor.close()
        conn.close()

        if user and user['password'] == password:  # In Produktion sollte hier ein Passwort-Hash-Vergleich stattfinden
            response = jsonify({
                "success": True,
                "message": "Login erfolgreich",
                "username": user['username'],
                "userId": user['id']
            })
            response.set_cookie('userId', str(user['id']))
            return response
        else:
            return jsonify({
                "success": False,
                "message": "Ungültige E-Mail oder Passwort"
            })

    except mysql.connector.Error as err:
        return jsonify({
            "success": False,
            "message": f"Datenbankfehler: {str(err)}"
        }) 