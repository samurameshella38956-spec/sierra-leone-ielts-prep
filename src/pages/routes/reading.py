from flask import Blueprint, jsonify

bp = Blueprint("reading", __name__, url_prefix="/reading")

# Example reading comprehension data
reading_passages = [
    {
        "id": 1,
        "title": "Global Education Trends",
        "passage": "IELTS is an international English test used by universities and employers worldwide...",
        "question": "What is the main purpose of IELTS?"
    },
    {
        "id": 2,
        "title": "Climate Change",
        "passage": "Climate change is one of the biggest challenges facing humanity today...",
        "question": "What is identified as the biggest challenge in the passage?"
    }
]

@bp.route("/practice", methods=["GET"])
def get_reading_practice():
    return jsonify(reading_passages)
