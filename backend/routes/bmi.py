from flask import Blueprint, request, jsonify

bmi_bp = Blueprint('bmi', __name__)

@bmi_bp.route('/calculate', methods=['POST'])
def calculate_bmi():
    data = request.get_json()
    weight = data.get('weight')  # in kilograms
    height = data.get('height')  # in centimeters

    if not weight or not height:
        return jsonify({"error": "Weight and height are required."}), 400

    try:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        category = categorize_bmi(bmi)
        return jsonify({"bmi": round(bmi, 2), "category": category})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"