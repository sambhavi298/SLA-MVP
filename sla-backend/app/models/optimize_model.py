from flask import current_app
from datetime import datetime

def insert_optimize_log(data):
    """
    Inserts an optimize log into the database.
    """
    db = current_app.config['DB']
    data['created_at'] = datetime.utcnow()
    result = db.optimize_logs.insert_one(data)
    return str(result.inserted_id)

def get_optimize_logs():
    """
    Retrieves all optimize logs from the database.
    """
    db = current_app.config['DB']
    logs = db.optimize_logs.find()
    return [{**log, "_id": str(log["_id"])} for log in logs]
