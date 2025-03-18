from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()

def create_user(username, email, password):
    hashed_password = generate_password_hash(password)
    user = {"username": username, "email": email, "password": hashed_password}
    mongo.db.users.insert_one(user)


def find_user_by_email(email):
    return mongo.db.users.find_one({"email": email})


def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)
