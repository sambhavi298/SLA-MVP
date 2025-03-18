from flask import Blueprint, request, jsonify
from app.services.ai_service import debug_code
from app.services.db_service import save_debug_result

debug_bp = Blueprint('debug', __name__)

@debug_bp.route('/', methods=['POST'])
def debug():
    data = request.get_json()
    code = data.get('code')
    if not code:
        return jsonify({"error": "No code provided"}), 400
    
    debug_result = debug_code(code)
    save_debug_result(debug_result)
    
    return jsonify({"result": debug_result}), 200
