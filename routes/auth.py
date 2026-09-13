from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User, Progress

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(email=data["email"], password=data["password"])  # hash password in production
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.password == data["password"]:  # use hashed check
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@bp.route("/progress", methods=["GET"])
@jwt_required()
def get_progress():
    user_id = get_jwt_identity()
    progress = Progress.query.filter_by(user_id=user_id).all()
    return jsonify([p.to_dict() for p in progress])

@bp.route("/progress", methods=["POST"])
@jwt_required()
def save_progress():
    user_id = get_jwt_identity()
    data = request.json
    progress = Progress(user_id=user_id, exam_type=data["exam_type"], score=data["score"])
    db.session.add(progress)
    db.session.commit()
    return jsonify({"message": "Progress saved"})
