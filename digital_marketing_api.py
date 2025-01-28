from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for metrics
metrics = {
    "website_visitors": 1200,
    "ad_clicks": 450,
    "conversions": 85,
    "roi": "250%"  # Return on Investment
}

# Mock campaigns data
campaigns = []

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Digital Marketing Dashboard API!"})

# Route for fetching metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({"success": True, "data": metrics})

# Route to add a new campaign
@app.route('/campaigns', methods=['POST'])
def add_campaign():
    data = request.json  # Get JSON data from the request
    if not data or 'name' not in data or 'budget' not in data:
        return jsonify({"success": False, "message": "Invalid data"}), 400

    # Add campaign to the list
    campaign = {
        "id": len(campaigns) + 1,  # Auto-increment ID
        "name": data['name'],
        "budget": data['budget'],
        "performance": data.get('performance', "Not available")
    }
    campaigns.append(campaign)
    return jsonify({"success": True, "message": "Campaign added!", "campaign": campaign}), 201

# Route to get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    return jsonify({"success": True, "data": campaigns})

# Route to search for campaigns by name
@app.route('/campaigns/search', methods=['GET'])
def search_campaigns():
    query = request.args.get('name')  # Get 'name' query param
    if not query:
        return jsonify({"success": False, "message": "Name query parameter is required"}), 400

    # Filter campaigns by name
    results = [c for c in campaigns if query.lower() in c['name'].lower()]
    return jsonify({"success": True, "data": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
