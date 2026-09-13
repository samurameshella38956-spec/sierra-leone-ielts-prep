from flask import Blueprint, request, jsonify

bp = Blueprint("exam", __name__, url_prefix="/exam")

# Example mock exam data
mock_exam = {
    "listening": [
        {"id": 1, "question": "Listen to the audio and answer: What is the speaker’s main point?", "audio": "/static/audio/sample1.mp3"}
    ],
    "reading": [
        {"id": 2, "passage": "IELTS is an international English test...", "question": "What is the purpose of IELTS?"}
    ],
    "writing": [
        {"id": 3, "task": "Write at least 150 words describing the chart below."}
    ],
    "speaking": [
        {"id": 4, "prompt": "Describe a memorable trip you have taken."}
    ]
}

@bp.route("/mock", methods=["GET"])
def get_mock_exam():
    return jsonify(mock_exam)

@bp.route("/submit", methods=["POST"])
def submit_exam():
    data = request.json
    # Here you would evaluate answers, store results, etc.
    return jsonify({"message": "Exam submitted successfully", "answers": data})
