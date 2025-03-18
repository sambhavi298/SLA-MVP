from app import mongo

def save_debug_result(result):
    mongo.db.debug.insert_one({"result": result})

def save_optimize_result(result):
    mongo.db.optimize.insert_one({"optimized_code": result})

def fetch_history():
    debug = list(mongo.db.debug.find({}, {"_id": 0}))
    optimize = list(mongo.db.optimize.find({}, {"_id": 0}))
    return {"debug": debug, "optimize": optimize}
