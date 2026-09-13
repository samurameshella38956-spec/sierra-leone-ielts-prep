from flask import Blueprint, request, jsonify
import os

bp = Blueprint("speaking", __name__, url_prefix="/speaking")

UPLOAD_FOLDER = "uploads/speaking"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/upload", methods=["POST"])
def upload_speaking():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Later: run AI evaluation on the audio file
    return jsonify({"message": "File uploaded successfully", "path": filepath})
