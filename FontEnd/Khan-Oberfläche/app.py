from flask import Flask, request, jsonify, send_from_directory
import os
import KI_searches_KIs as ki  # Import your script (rename the file to use underscores)
import markdown  # Add this import for Markdown to HTML conversion

app = Flask(__name__)
# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # List all files in the current directory to help debug
    files = os.listdir(BASE_DIR)
    print(f"Files in directory: {files}")

    # Look for HTML files
    html_files = [f for f in files if f.endswith('.html')]
    print(f"HTML files found: {html_files}")

    # If Search_AI.html exists, serve it
    if 'User.html' in html_files:
        return send_from_directory(BASE_DIR, 'User.html')
    # If index.html exists, serve it
    elif 'index.html' in html_files:
        return send_from_directory(BASE_DIR, 'index.html')
    # If no suitable HTML file is found
    else:
        return "No HTML file found. Please make sure Search_AI.html or index.html is in the same directory as app.py."

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