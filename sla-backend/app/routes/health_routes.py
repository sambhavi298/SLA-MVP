# /routes/health_routes.py

from flask import Blueprint, jsonify
from app import mongo

health_bp = Blueprint('health', __name__)

@health_bp.route('/test-db')
def test_db():
    db = mongo_client['sla_db']
    test_collection = db['test_collection']
    test_document = {"message": "MongoDB Atlas connection successful!"}
    test_collection.insert_one(test_document)
    result = test_collection.find_one({"message": "MongoDB Atlas connection successful!"})
    return jsonify({"status": "success", "data": result["message"]})
