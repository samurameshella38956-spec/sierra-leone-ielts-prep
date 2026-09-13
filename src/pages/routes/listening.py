from flask import Blueprint, jsonify

bp = Blueprint("listening", __name__, url_prefix="/listening")

# Example listening practice data
listening_questions = [
    {
        "id": 1,
        "question": "What is the speaker’s main point?",
        "audio": "/static/audio/sample1.mp3"
    },
    {
        "id": 2,
        "question": "What does the speaker suggest about studying abroad?",
        "audio": "/static/audio/sample2.mp3"
    }
]

@bp.route("/practice", methods=["GET"])
def get_listening_practice():
    return jsonify(listening_questions)
