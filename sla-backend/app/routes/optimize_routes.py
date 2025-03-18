from flask import Blueprint, request, jsonify
from app.models.optimize_model import insert_optimize_log, get_optimize_logs

optimize_bp = Blueprint('optimize', __name__)

@optimize_bp.route('/', methods=['POST'])
def create_optimize_log():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "Code data is required"}), 400

    log = {
        "code": data['code'],
        "optimized_code": data.get('optimized_code', ''),
        "timestamp": data.get('timestamp', '')
    }
    inserted_id = insert_optimize_log(log)
    return jsonify({"message": "Optimize log created", "id": str(inserted_id)}), 201

@optimize_bp.route('/', methods=['GET'])
def fetch_optimize_logs():
    logs = get_optimize_logs()
    return jsonify({"optimize_logs": logs}), 200
