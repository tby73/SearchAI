# Whenever there is "***" at the end of a comment, then DO NOT DELETE THAT COMMENT   ***
# TO DO next time:    ***
# thermal paste / case fans / ...   ***
# images of parts   ***
# https://de.pcpartpicker.com/search/?q=thermal+compound&page=1 ***
from flask import Flask, render_template, request, jsonify, redirect, url_for
from functools import wraps
from pypartpicker import Scraper
import requests
import json
import re
from fuzzywuzzy import fuzz
import mysql.connector
from login import check_login
from register import register_user

app = Flask(__name__, static_folder='static')
pcpp = Scraper()

# OpenAI API endpoint and API key
openai_endpoint = "https://api.openai.com/v1/chat/completions"
openai_api_key = "your-api-key-here"

# Add these configurations after your existing configurations
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "p2c-data"
}

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get('userId') is None:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if request.cookies.get('userId'):
        return redirect(url_for('main'))
    return render_template('creatacc.html')

@app.route('/main')
@login_required
def main():
    return render_template('Front_End.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    response = check_login(data['email'], data['password'])
    return response

@app.route('/logout')
def logout():
    response = redirect(url_for('index'))
    response.delete_cookie('userId')
    return response

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data['username'], data['email'], data['password'])

def get_price_ranges(budget):
    price_range_prompt = f"""
    For a gaming PC with a total budget of €{budget}, provide price ranges for each component.
    Allocate the budget like this, with minimum prices scaled based on total budget:
    - CPU: min from €{max(200, budget * 0.1)}, max 25-30% of budget
    - GPU: min from €{max(300, budget * 0.15)}, max 80% of budget
    - Motherboard: min from €{max(100, budget * 0.05)}, max 15% of budget
    - RAM: min should start very low (€40-€60) for budget builds, max 10% of budget
    - Storage: min from €{max(80, budget * 0.02)}, max 10% of budget
    - Power Supply: min from €{max(80, budget * 0.02)}, max 10% of budget
    - Case: min from €{max(80, budget * 0.02)}, max 10% of budget
    - CPU Cooler: min from €{max(60, budget * 0.02)}, max 10% of budget
    - Case Fans: min from €{max(20, budget * 0.01)}, max 5% of budget
    - Thermal Paste: min from €{max(5, budget * 0.005)}, max 2% of budget

    For high budgets (>€3000), allow the GPU to take up to 80% of the budget to accommodate high-end cards like the RTX 4090.

    Return ONLY a JSON object with this exact structure:
    {{
        "CPU": {{"min": number, "max": number}},
        "GPU": {{"min": number, "max": number}},
        "Motherboard": {{"min": number, "max": number}},
        "RAM": {{"min": number, "max": number}},
        "Storage": {{"min": number, "max": number}},
        "Power Supply": {{"min": number, "max": number}},
        "Case": {{"min": number, "max": number}},
        "CPU Cooler": {{"min": number, "max": number}},
        "Case Fans": {{"min": number, "max": number}},
        "Thermal Paste": {{"min": number, "max": number}}
    }}
    The sum of all maximum prices should not exceed €{budget}.
    IMPORTANT: For RAM, ensure the minimum price is low enough to include basic options, especially for budget builds.
    The range between min and max should be wide enough to give multiple options.
    """

    try:
        response = requests.post(
            openai_endpoint,
            headers={'Authorization': f'Bearer {openai_api_key}', 'Content-Type': 'application/json'},
            json={
                #'model': 'gpt-4o-mini-2024-07-18', ***
                'model': 'gpt-4o-mini',
                'messages': [{'role': 'user', 'content': price_range_prompt}],
                'temperature': 0.7
            }
        )

        if response.status_code != 200:
            print(f"OpenAI API error: {response.status_code}")
            print(f"Response: {response.text}")
            raise Exception("Failed to get price ranges from OpenAI")

        # Extract the JSON content from the response
        content = response.json()['choices'][0]['message']['content'].strip()

        # Remove any markdown formatting if present
        if content.startswith('```json'):
            content = content[7:-3].strip()
        elif content.startswith('```'):
            content = content[3:-3].strip()

        print("\nPrice Ranges from AI:")
        print(content)

        try:
            price_ranges = json.loads(content)

            # Validate the structure
            required_keys = ["CPU", "GPU", "Motherboard", "RAM", "Storage", "Power Supply", "Case", "CPU Cooler", "Case Fans", "Thermal Paste"]
            if not all(key in price_ranges for key in required_keys):
                raise ValueError("Missing required components in price ranges")

            # Validate the ranges
            total_max = sum(comp['max'] for comp in price_ranges.values())
            print(f"\nTotal maximum budget: €{total_max} (Target: €{budget})")

            return price_ranges

        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise

    except Exception as e:
        print(f"Error in get_price_ranges: {str(e)}")
        # Provide default price ranges based on budget percentages
        default_ranges = {
            "CPU": {"min": budget * 0.20, "max": budget * 0.30},
            "GPU": {"min": budget * 0.30, "max": budget * 0.40},
            "Motherboard": {"min": budget * 0.10, "max": budget * 0.15},
            "RAM": {"min": budget * 0.05, "max": budget * 0.10},
            "Storage": {"min": budget * 0.05, "max": budget * 0.10},
            "Power Supply": {"min": budget * 0.05, "max": budget * 0.10},
            "Case": {"min": budget * 0.05, "max": budget * 0.10},
            "CPU Cooler": {"min": budget * 0.05, "max": budget * 0.10},
            "Case Fans": {"min": budget * 0.01, "max": budget * 0.05},
            "Thermal Paste": {"min": budget * 0.005, "max": budget * 0.02}
        }
        print("\nUsing default price ranges:")
        print(json.dumps(default_ranges, indent=2))
        return default_ranges

def get_component_prices(component_type, region="de", cpu_preference=None, price_range=None):
    prices = []

    if component_type == "cpu":
        if cpu_preference == "Intel":
            # Search for specific high-end models first
            search_terms = ["i9-14900K", "i9-13900K", "i9-14900KF", "i9-13900KF"]
            for term in search_terms:
                parts = pcpp.part_search(term, type="cpu", region=region)
                for part in parts:
                    if part.price and part.price != "None" and "Intel Core" in part.name:
                        price = float(part.price.replace("€", "").replace(",", "").strip())
                        if price_range and price_range["min"] <= price <= price_range["max"]:
                            prices.append({
                                "name": part.name,
                                "price": price,
                                "url": part.url
                            })

            # Then do the general tier search
            for cpu_tier in ["i9", "i7", "i5", "i3"]:
                parts = pcpp.part_search(cpu_tier, type="cpu", region=region)
                for part in parts:
                    if part.price and part.price != "None" and "Intel Core" in part.name:
                        price = float(part.price.replace("€", "").replace(",", "").strip())
                        if price_range and price_range["min"] <= price <= price_range["max"]:
                            prices.append({
                                "name": part.name,
                                "price": price,
                                "url": part.url
                            })
        elif cpu_preference == "AMD":
            # Search for specific high-end models first
            search_terms = ["Ryzen 9 7950X3D", "Ryzen 9 7900X3D", "Ryzen 7 7800X3D"]
            for term in search_terms:
                parts = pcpp.part_search(term, type="cpu", region=region)
                for part in parts:
                    if part.price and part.price != "None" and "AMD Ryzen" in part.name:
                        price = float(part.price.replace("€", "").replace(",", "").strip())
                        if price_range and price_range["min"] <= price <= price_range["max"]:
                            prices.append({
                                "name": part.name,
                                "price": price,
                                "url": part.url
                            })

            # Then do the general tier search
            for cpu_tier in ["Ryzen 9", "Ryzen 7", "Ryzen 5", "Ryzen 3"]:
                parts = pcpp.part_search(cpu_tier, type="cpu", region=region)
                for part in parts:
                    if part.price and part.price != "None" and "AMD Ryzen" in part.name:
                        price = float(part.price.replace("€", "").replace(",", "").strip())
                        if price_range and price_range["min"] <= price <= price_range["max"]:
                            prices.append({
                                "name": part.name,
                                "price": price,
                                "url": part.url
                            })
    elif component_type == "video card":
        # GPU search terms, starting from high-end and going down to 3060
        search_terms = ["4090", "4080", "4070", "4060", "3060", "RX 7900", "RX 7800", "RX 7700", "RX 7600", "RX 6900", "RX 6800", "RX 6700"]
        print("\nSearching for GPUs:")  # Debug print
        for term in search_terms:
            parts = pcpp.part_search(term, type="video card", region=region)
            print(f"\nResults for {term}:")  # Debug print
            for part in parts:
                if part.price and part.price != "None":
                    price = float(part.price.replace("€", "").replace(",", "").strip())
                    print(f"Found: {part.name} at €{price}")  # Debug print
                    if price_range and price_range["min"] <= price <= price_range["max"]:
                        prices.append({
                            "name": part.name,
                            "price": price,
                            "url": part.url
                        })

    elif component_type == "case fans":
        # Case Fans search
        search_terms = ["fan"]
        for term in search_terms:
            parts = pcpp.part_search(term, type="case fan", region=region)
            for part in parts:
                if part.price and part.price != "None":
                    price = float(part.price.replace("€", "").replace(",", "").strip())
                    if price_range and price_range["min"] <= price <= price_range["max"]:
                        prices.append({
                            "name": part.name,
                            "price": price,
                            "url": part.url
                        })

    elif component_type == "thermal paste":
        # Thermal Paste search
        search_terms = ["thermal"]
        for term in search_terms:
            parts = pcpp.part_search(term, type="thermal compound", region=region)
            for part in parts:
                if part.price and part.price != "None":
                    price = float(part.price.replace("€", "").replace(",", "").strip())
                    if price_range and price_range["min"] <= price <= price_range["max"]:
                        prices.append({
                            "name": part.name,
                            "price": price,
                            "url": part.url
                        })

    else:
        parts = pcpp.part_search(component_type, region=region)
        for part in parts:
            if part.price and part.price != "None":
                price = float(part.price.replace("€", "").replace(",", "").strip())
                if price_range and price_range["min"] <= price <= price_range["max"]:
                    prices.append({
                        "name": part.name,
                        "price": price,
                        "url": part.url
                    })

    return prices

@app.route('/api/build-suggestion', methods=['POST'])
def build_suggestion():
    try:
        data = request.get_json()
        budget = float(data.get('budget'))
        purpose = data.get('purpose')
        additional_info = data.get('additional_info')
        cpu_preference = "Intel" if "CPU Preference: Intel" in additional_info else "AMD"

        # Get price ranges from AI
        price_ranges = get_price_ranges(budget)

        # Get components within price ranges
        component_prices = {
            "CPU": get_component_prices("cpu", cpu_preference=cpu_preference, price_range=price_ranges["CPU"]),
            "Motherboard": get_component_prices("motherboard", price_range=price_ranges["Motherboard"]),
            "RAM": get_component_prices("memory", price_range=price_ranges["RAM"]),
            "GPU": get_component_prices("video card", price_range=price_ranges["GPU"]),
            "Storage": get_component_prices("internal hard drive", price_range=price_ranges["Storage"]),
            "Power Supply": get_component_prices("power supply", price_range=price_ranges["Power Supply"]),
            "Case": get_component_prices("case", price_range=price_ranges["Case"]),
            "CPU Cooler": get_component_prices("cpu cooler", price_range=price_ranges["CPU Cooler"]),
            "Case Fans": get_component_prices("case fans", price_range=price_ranges["Case Fans"]),
            "Thermal Paste": get_component_prices("thermal paste", price_range=price_ranges["Thermal Paste"])
        }

        # Debug print component prices
        print("\nComponent prices for AI:")
        for component_type, prices in component_prices.items():
            print(f"\n{component_type}:")
            for p in prices[:10]:
                print(f"{p['name']}: €{p['price']}")

        # Create a prompt with real market prices
        initial_prompt = f"""
        You are a PC building expert. Create a PC build configuration for a {purpose} PC with a target budget of €{budget} and these requirements: {additional_info}.
        
        IMPORTANT GUIDELINES:
        1. Try to keep the total cost as close to €{budget} as possible
        2. It's okay to go slightly over budget (up to 5%) if it means getting significantly better components
        3. When selecting the GPU, if it takes more than 60% of the budget, try to optimize other component costs
        4. For CPUs and GPUs, prefer the newest generation within reasonable price ranges
        5. Include at least 3 case fans for proper airflow
        6. Include thermal paste for the CPU cooler
        7. Aim for the best performance while staying as close to budget as possible
        
        Use ONLY components from these real market prices (format: name: price in EUR):

        CPUs:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['CPU'][:10]])}

        Motherboards:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Motherboard'][:10]])}

        RAM:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['RAM'][:10]])}

        GPUs:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['GPU'][:10]])}

        Storage:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Storage'][:10]])}

        Power Supplies:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Power Supply'][:10]])}

        Cases:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Case'][:10]])}

        CPU Coolers:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['CPU Cooler'][:10]])}
        
        Case Fans:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Case Fans'][:10]])}

        Thermal Paste:
        {', '.join([f"{p['name']}: €{p['price']}" for p in component_prices['Thermal Paste'][:10]])}

        Return a JSON object with exactly this structure, using ONLY the components and prices listed above:
        {{
            "build": [
                {{
                    "name": "Component Name",
                    "type": "Component Type",
                    "price": number,
                    "description": "Component Description",
                    "url": "Component URL"
                }}
            ],
            "total_price": number
        }}

        Return ONLY the JSON object, no additional text, explanations, or markdown formatting.
        """

        budget_response = requests.post(
            openai_endpoint,
            headers={'Authorization': f'Bearer {openai_api_key}', 'Content-Type': 'application/json'},
            json={
                'model': 'gpt-4o-mini',
                'messages': [{'role': 'user', 'content': initial_prompt}],
                'temperature': 0.7,
                'max_tokens': 4000  # Increased from 2000 to 4000
            }
        )

        if budget_response.status_code != 200:
            return jsonify({'error': 'Failed to get budget allocation from OpenAI'}), 500

        content = budget_response.json()['choices'][0]['message']['content'].strip()

        # Debug print AI response
        print("\nAI Response:")
        print(content)

        # Clean up the JSON response
        if content.startswith('```json'):
            content = content[7:-3].strip()
        elif content.startswith('```'):
            content = content[3:-3].strip()

        try:
            # Validate JSON structure before parsing
            if not content.endswith('}'):
                content = content + '}'  # Close the main object if it's missing
            
            # Fix truncated Case Fan entries
            if '"Case Fan"' in content and not content.endswith('"}]}'):
                last_complete_component = content.rfind('"}')
                if last_complete_component != -1:
                    content = content[:last_complete_component+2] + ']}'

            # Remove any incomplete components
            if '{"name":' in content and not content.endswith('"}]}'):
                last_complete_component = content.rfind('"}')
                if last_complete_component != -1:
                    content = content[:last_complete_component+2] + ']}'

            build_data = json.loads(content)

            # Validate required fields
            if not isinstance(build_data, dict) or 'build' not in build_data:
                raise ValueError("Invalid build data structure")

            # Ensure all components have required fields
            for component in build_data['build']:
                required_fields = ['name', 'type', 'price', 'description', 'url']
                if not all(field in component for field in required_fields):
                    raise ValueError(f"Missing required fields in component: {component}")

            # Verify that all components exist in our real price data
            for component in build_data['build']:
                component_type = component['type']
                component_name = component['name']
                component_price = component['price']

                # Map component types to match our dictionary keys
                type_mapping = {
                    "Case Fan": "Case Fans",
                    "Case Fans": "Case Fans",
                    "GPU": "GPU",
                    "video card": "GPU",
                }

                # Use the mapped type or the original if no mapping exists
                lookup_type = type_mapping.get(component_type, component_type)

                # Extract CFM if present in the name (for Case Fans)
                suggested_cfm = None
                if component_type in ["Case Fan", "Case Fans"]:  # Handle both forms
                    match = re.search(r"(\d+\.?\d*) CFM", component_name)
                    if match:
                        suggested_cfm = float(match.group(1))

                # More flexible matching logic with scoring
                best_match = None
                best_score = -1

                try:
                    for p in component_prices[lookup_type]:  # Add try-except here
                        score = 0
                        # Full Name Similarity (using a simple ratio for now)
                        full_name_similarity = fuzz.ratio(component_name.lower(), p['name'].lower())
                        score += full_name_similarity

                        # Word matching (penalize if words are missing)
                        for word in component_name.split():
                            if word.lower() in p['name'].lower():
                                score += 1
                            else:
                                score -= 2  # Penalize missing words

                        # Price proximity check (within a tolerance, e.g., 10%)
                        if abs(p['price'] - component_price) <= component_price * 0.1:
                            score += 10  # Give extra weight to price matching

                        # CFM Proximity check (for Case Fans, within a tolerance, e.g., 5 CFM)
                        if component_type == "Case Fan" and suggested_cfm is not None:
                            match = re.search(r"(\d+\.?\d*) CFM", p['name'])
                            if match:
                                scraped_cfm = float(match.group(1))
                                if abs(scraped_cfm - suggested_cfm) <= 5:
                                    score += 8

                        if score > best_score:
                            best_score = score
                            best_match = p
                except KeyError:
                    print(f"Component type not found: {lookup_type} (original: {component_type})")
                    # Try alternative lookup if the first one fails
                    alternative_type = "Case Fans" if lookup_type == "Case Fan" else lookup_type
                    if alternative_type in component_prices:
                        for p in component_prices[alternative_type]:
                            score = 0
                            # Full Name Similarity (using a simple ratio for now)
                            full_name_similarity = fuzz.ratio(component_name.lower(), p['name'].lower())
                            score += full_name_similarity

                            # Word matching (penalize if words are missing)
                            for word in component_name.split():
                                if word.lower() in p['name'].lower():
                                    score += 1
                                else:
                                    score -= 2  # Penalize missing words

                            # Price proximity check (within a tolerance, e.g., 10%)
                            if abs(p['price'] - component_price) <= component_price * 0.1:
                                score += 10  # Give extra weight to price matching

                            # CFM Proximity check (for Case Fans, within a tolerance, e.g., 5 CFM)
                            if component_type == "Case Fan" and suggested_cfm is not None:
                                match = re.search(r"(\d+\.?\d*) CFM", p['name'])
                                if match:
                                    scraped_cfm = float(match.group(1))
                                    if abs(scraped_cfm - suggested_cfm) <= 5:
                                        score += 8

                            if score > best_score:
                                best_score = score
                                best_match = p

                if best_match is None:
                    print(f"Error in build suggestion: '{component_type}'")
                    return jsonify({'error': f'Component not found in market prices: {component_name}'}), 400

                # Update with real name, price, and URL from the best match
                component['name'] = best_match['name']
                component['price'] = best_match['price']
                component['url'] = best_match['url']

            # Recalculate total price based on real prices
            real_total = sum(component['price'] for component in build_data['build'])
            build_data['total_price'] = round(real_total, 2)  # Round to 2 decimal places

            # Debug print for price calculation
            print("\nPrice Calculation:")
            for component in build_data['build']:
                print(f"{component['type']}: €{component['price']}")
            print(f"Total: €{build_data['total_price']}")

            return jsonify(build_data), 200

        except json.JSONDecodeError as e:
            print(f"\nJSON Decode Error: {str(e)}")
            print(f"Problematic content: {content}")
            # Try to recover from common JSON errors
            try:
                # Remove any trailing commas
                content = re.sub(r',\s*([}\]])', r'\1', content)
                # Ensure proper array/object closure
                if content.count('{') > content.count('}'):
                    content += '}' * (content.count('{') - content.count('}'))
                if content.count('[') > content.count(']'):
                    content += ']' * (content.count('[') - content.count(']'))
                build_data = json.loads(content)
                return jsonify(build_data), 200
            except:
                return jsonify({'error': f'Invalid JSON response from AI: {str(e)}'}), 500

    except Exception as e:
        print("Error in build suggestion:", str(e))
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/save-config', methods=['POST'])
def save_config():
    try:
        data = request.get_json()
        config_name = data.get('name')
        config_content = data.get('content')
        user_id = data.get('userId')

        if not config_name or not config_content or not user_id:
            return jsonify({'success': False, 'error': 'Missing required data'}), 400

        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert the configuration with user ID
        sql = "INSERT INTO usercreations (configuration, usercreationsid) VALUES (%s, %s)"
        cursor.execute(sql, (config_content.encode(), user_id))
        
        # Commit the transaction
        conn.commit()

        # Close connections
        cursor.close()
        conn.close()

        return jsonify({'success': True}), 200

    except Exception as e:
        print(f"Error saving configuration: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/get-configs', methods=['GET'])
def get_configs():
    try:
        user_id = request.cookies.get('userId')
        if not user_id:
            return jsonify({'success': False, 'error': 'Not logged in'}), 401

        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Get configurations for the user
        sql = "SELECT * FROM usercreations WHERE usercreationsid = %s"
        cursor.execute(sql, (user_id,))
        configs = cursor.fetchall()

        # Close connections
        cursor.close()
        conn.close()

        # Process configurations
        processed_configs = []
        for config in configs:
            try:
                # Decode the configuration content
                content = config['configuration'].decode('utf-8')
                processed_configs.append({
                    'id': config['id'],
                    'content': content,
                    'created_at': config['created_at'].isoformat() if config.get('created_at') else None
                })
            except Exception as e:
                print(f"Error processing config {config.get('id')}: {str(e)}")
                continue

        return jsonify({'success': True, 'configurations': processed_configs})

    except Exception as e:
        print(f"Error fetching configurations: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/user-info')
@login_required
def get_user_info():
    try:
        user_id = request.cookies.get('userId')
        
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Get user information
        sql = "SELECT username, email FROM userinformations WHERE id = %s"
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()

        # Close connections
        cursor.close()
        conn.close()

        if user:
            return jsonify({
                'success': True,
                'username': user['username'],
                'email': user['email']
            })
        else:
            return jsonify({
                'success': False,
                'message': 'User not found'
            }), 404

    except Exception as e:
        print(f"Error fetching user info: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Error fetching user information'
        }), 500

@app.route('/api/change-password', methods=['POST'])
@login_required
def change_password():
    try:
        data = request.get_json()
        current_password = data.get('currentPassword')
        new_password = data.get('newPassword')
        user_id = request.cookies.get('userId')

        if not current_password or not new_password:
            return jsonify({
                'success': False,
                'message': 'Missing required fields'
            }), 400

        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Verify current password
        sql = "SELECT password FROM userinformations WHERE id = %s"
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()

        if not user or user['password'] != current_password:
            cursor.close()
            conn.close()
            return jsonify({
                'success': False,
                'message': 'Current password is incorrect'
            }), 401

        # Update password
        update_sql = "UPDATE userinformations SET password = %s WHERE id = %s"
        cursor.execute(update_sql, (new_password, user_id))
        conn.commit()

        # Close connections
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'message': 'Password updated successfully'
        })

    except Exception as e:
        print(f"Error changing password: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Error changing password'
        }), 500

@app.route('/api/generate-news', methods=['GET'])
def generate_news():
    try:
        # Get the topic from request parameters
        topic = request.args.get('topic')
        
        if topic:
            # Create a focused prompt for the specific topic
            prompt = f"""Generate a detailed news article focusing specifically on {topic} in the context of PC hardware.
            The article should be comprehensive and cover:

            1. Main Topic Analysis ({topic}):
            - Current market status and availability
            - Performance benchmarks and comparisons
            - Price trends and value proposition
            - Common use cases and target audience
            - Known issues or limitations
            - Future outlook and potential developments

            2. Related Components and Compatibility:
            - How {topic} interacts with other PC components
            - Recommended system configurations
            - Compatibility considerations
            - Alternative options in the same category

            3. User Experience and Reviews:
            - Real-world performance data
            - User feedback and common experiences
            - Professional reviews and benchmarks
            - Tips for optimal usage

            4. Market Context:
            - Position in the current market
            - Competition and alternatives
            - Price history and trends
            - Availability and supply chain status

            Format the response in clean HTML with:
            - Clear section headings (h2, h3)
            - Well-structured paragraphs
            - Bullet points where appropriate
            - Comparison tables where relevant
            - Bold text for important points
            - Proper spacing between sections

            Make it factual, detailed, and informative, focusing specifically on {topic} and directly related aspects.
            Include specific model numbers, prices, and performance metrics where relevant."""

            system_content = f"You are a tech journalist specializing in PC hardware, with particular expertise in {topic}. Write a detailed, well-researched article focusing specifically on {topic} and closely related aspects."
        else:
            # Use the general prompt for no specific topic
            prompt = """Generate an extensive news page about the latest developments in computer hardware and PC components. 
            Create multiple detailed sections covering:

            1. Latest CPU Developments:
            - New releases from both Intel and AMD
            - Detailed performance comparisons
            - Price-to-performance analysis
            - Future CPU roadmaps and expectations

            2. GPU Market Analysis:
            - Recent graphics card launches
            - Price trends and availability
            - Performance benchmarks
            - Mining impact on GPU market
            - Future GPU technologies

            3. Storage Technology Updates:
            - New SSD technologies
            - Price per GB trends
            - PCIe 5.0 storage developments
            - HDD vs SSD market analysis

            4. RAM and Memory:
            - DDR5 adoption and performance
            - Price trends
            - New technologies and improvements
            - Future memory standards

            5. Cooling Solutions:
            - Latest AIO coolers
            - Air cooling innovations
            - Thermal paste developments
            - Case airflow optimization

            6. Power Supply Developments:
            - New efficiency standards
            - ATX 3.0 adoption
            - Market trends and pricing

            7. Case and Form Factor Trends:
            - New case designs
            - Airflow optimization trends
            - Size and format preferences
            - Material innovations

            8. Market Analysis and Future Outlook:
            - Overall component price trends
            - Supply chain updates
            - Future technology predictions
            - Industry challenges and opportunities

            Format the response in clean HTML with:
            - Clear section headings (h2, h3)
            - Well-structured paragraphs
            - Bullet points where appropriate
            - Price comparisons in tables where relevant
            - Bold text for important points
            - Proper spacing between sections

            Make it factual, detailed, and informative, focusing on real products and developments.
            Include specific model numbers, prices, and performance metrics where relevant."""

            system_content = "You are a tech journalist specializing in PC hardware. Write detailed, well-researched articles with extensive coverage."

        # Call OpenAI API with increased token limit
        response = requests.post(
            openai_endpoint,
            headers={
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 4000  # Increased token limit for longer content
            }
        )

        if response.status_code == 200:
            news_content = response.json()['choices'][0]['message']['content']
            return jsonify({'success': True, 'content': news_content})
        else:
            return jsonify({'success': False, 'error': 'Failed to generate news content'}), 500

    except Exception as e:
        print(f"Error generating news: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)