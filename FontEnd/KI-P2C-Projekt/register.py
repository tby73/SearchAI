import mysql.connector
import json
from flask import jsonify

def register_user(username, email, password):
    try:
        # Verbindung zur Datenbank herstellen
        # Beachte: Nutzung von 'localhost' und root-Benutzer ohne Passwort ist unsicher. Verwende Umgebungsvariablen für Zugangsdaten.
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="p2c-data"  # Stelle sicher, dass die Datenbank 'p2c-data' existiert und zugänglich ist.
        )
        cursor = conn.cursor(dictionary=True)

        # Prüfen ob E-Mail bereits existiert
        # Dieser SQL-Befehl prüft, ob die E-Mail in der Tabelle vorhanden ist.
        # Sicherstellen, dass die Spalte 'email' in der Tabelle indiziert ist, um die Abfrageleistung zu verbessern.
        check_sql = "SELECT * FROM userinformations WHERE email = %s"
        cursor.execute(check_sql, (email,))
        if cursor.fetchone():  # Überprüfung, ob ein Benutzer mit dieser E-Mail existiert
            cursor.close()
            conn.close()
            return jsonify({
                "success": False,
                "message": "Diese E-Mail-Adresse wird bereits verwendet"
            })

        # Neuen Benutzer anlegen
        # Achtung: Passwörter sollten niemals im Klartext gespeichert werden. Nutze eine Hashing-Bibliothek wie bcrypt.
        insert_sql = "INSERT INTO userinformations (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_sql, (username, email, password))
        conn.commit()  # Änderungen dauerhaft in der Datenbank speichern

        cursor.close()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Registrierung erfolgreich"
        })

    except mysql.connector.Error as err:
        # Fehlerbehandlung: Datenbankfehler abfangen und Benutzer informieren.
        # Es könnte hilfreich sein, diese Fehler zusätzlich zu protokollieren.
        return jsonify({
            "success": False,
            "message": f"Datenbankfehler: {str(err)}"
        })
