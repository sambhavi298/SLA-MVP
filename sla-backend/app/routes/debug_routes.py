from flask import Blueprint, request, jsonify, current_app

debug_bp = Blueprint('debug', __name__, url_prefix='/api/debug')

@debug_bp.route('/', methods=['POST'])
def debug():
    try:
        data = request.get_json()
        if not data or 'code' not in data:
            return jsonify({"error": "Missing 'code' in request body"}), 400

        # Placeholder debug logic
        current_app.logger.info(f"Debugging code: {data['code']}")
        return jsonify({"message": "Debug successful", "code": data['code']})
    except Exception as e:
        current_app.logger.error(f"Debug route error: {e}")
        return jsonify({"error": "Failed to debug code"}), 500