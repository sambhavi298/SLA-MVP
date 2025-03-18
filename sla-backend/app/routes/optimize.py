from flask import Blueprint, request, jsonify
from app.services.ai_service import optimize_code
from app.services.db_service import save_optimize_result

optimize_bp = Blueprint('optimize', __name__)

@optimize_bp.route('/', methods=['POST'])
def optimize():
    data = request.get_json()
    code = data.get('code')
    if not code:
        return jsonify({"error": "No code provided"}), 400

    optimized_code = optimize_code(code)
    save_optimize_result(optimized_code)
    
    return jsonify({"optimized_code": optimized_code}), 200
