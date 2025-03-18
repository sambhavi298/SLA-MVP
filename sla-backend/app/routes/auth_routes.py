from flask import Blueprint, request, jsonify
from ..models.user_model import create_user, find_user_by_email, verify_password
import jwt
import datetime
from ..config import Config
from ..utils.auth_utils import token_required

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if find_user_by_email(data['email']):
        return jsonify({'error': 'User already exists'}), 400

    create_user(data['username'], data['email'], data['password'])
    return jsonify({'message': 'User registered successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = find_user_by_email(data['email'])

    if not user or not verify_password(data['password'], user['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({
        'user_id': str(user['_id']),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({'token': token}), 200


@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user_id):
    return jsonify({"message": f"Hello user {current_user_id}, you accessed a protected route!"}), 200
