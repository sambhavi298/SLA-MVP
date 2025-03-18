from flask import Blueprint, jsonify
from app.services.db_service import fetch_history

history_bp = Blueprint('history', __name__)

@history_bp.route('/', methods=['GET'])
def get_history():
    history = fetch_history()
    return jsonify({"history": history}), 200
