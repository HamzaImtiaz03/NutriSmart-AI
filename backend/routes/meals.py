from flask import Blueprint, request, jsonify
import requests
import os

meals_bp = Blueprint('meals', __name__)

@meals_bp.route('/analyze', methods=['POST'])
def analyze_meal():
    data = request.get_json()
    meal_text = data.get('meal')

    if not meal_text:
        return jsonify({"error": "Meal input is required"}), 400

    api_key = os.getenv('CALORIE_NINJAS_API_KEY')
    if not api_key:
        return jsonify({"error": "Missing CalorieNinjas API key in environment"}), 500

    url = f"https://api.calorieninjas.com/v1/nutrition?query={meal_text}"
    headers = {'X-Api-Key': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": "API request failed", "details": str(err)}), 500
