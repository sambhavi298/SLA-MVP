from flask import current_app
from datetime import datetime

def insert_debug_log(data):
    """
    Inserts a debug log into the database.
    """
    db = current_app.config['DB']
    data['created_at'] = datetime.utcnow()
    result = db.debug_logs.insert_one(data)
    return str(result.inserted_id)

def get_debug_logs():
    """
    Retrieves all debug logs from the database.
    """
    db = current_app.config['DB']
    logs = db.debug_logs.find()
    return [{**log, "_id": str(log["_id"])} for log in logs]
