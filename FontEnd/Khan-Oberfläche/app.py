from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import mysql.connector
from flask_cors import CORS
import KI_searches_KIs as ki  # Import your script (rename the file to use underscores)
import markdown  # Add this import for Markdown to HTML conversion

app = Flask(__name__, template_folder="template")
CORS(app)

# Database configuration
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="searchai_maindb"
    )

# ========== HTML ROUTES ==========
@app.route('/')
def home():
    return render_template('User.html')

@app.route('/admin')
def admin():
    return render_template('Admin.html')

# ========== API ROUTES ==========
@app.route('/api/add-ai', methods=['POST'])
def add_ai():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        category = data.get('category')
        url = data.get('url')

        if not all([name, description, category, url]):
            return jsonify({'success': False, 'message': 'Missing required fields'})

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ai_models (name, description, category, url)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, description, category, url))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': 'AI added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/get-ais', methods=['GET'])
def get_ais():
    try:
        search_query = request.args.get('query', '')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        if search_query:
            search_query = f"%{search_query}%"
            query = """
                SELECT * FROM ai_models 
                WHERE name LIKE %s 
                OR description LIKE %s 
                OR category LIKE %s
            """
            cursor.execute(query, (search_query, search_query, search_query))
        else:
            cursor.execute("SELECT * FROM ai_models")
        
        ais = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'ais': ais})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/api/search-ai', methods=['POST'])
def search_ai():
    try:
        data = request.json
        query = data.get('query', '')

        if not query:
            return jsonify({'success': False, 'message': 'No query provided'})

        # Generate search keywords
        search_keywords = ki.generate_search_keywords(query, ki.OPENAI_API_KEY)

        # Get search results
        search_results = ki.get_google_search_results(
            search_keywords,
            ki.GOOGLE_API_KEY,
            ki.CUSTOM_SEARCH_ENGINE_ID,
            count=5
        )

        if not search_results:
            return jsonify({'success': False, 'message': 'No search results found'})

        # Summarize results
        summary = ki.summarize_results_with_chatgpt(
            search_results,
            query,
            ki.OPENAI_API_KEY
        )

        # Format the summary as HTML, properly converting Markdown
        html_content = markdown.markdown(summary)
        formatted_results = f"<h3>AI Solutions for: {query}</h3><div>{html_content}</div>"

        return jsonify({'success': True, 'results': formatted_results})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5500)