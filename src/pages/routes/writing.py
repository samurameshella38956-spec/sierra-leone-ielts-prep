from flask import Blueprint, request, jsonify

bp = Blueprint("writing", __name__, url_prefix="/writing")

# Example IELTS Writing tasks
writing_tasks = {
    "task1": {
        "id": 1,
        "type": "Task 1",
        "prompt": "Write at least 150 words describing the chart below showing IELTS test takers by country."
    },
    "task2": {
        "id": 2,
        "type": "Task 2",
        "prompt": "Some people think studying abroad is better than studying locally. Discuss both views and give your opinion."
    }
}

@bp.route("/practice", methods=["GET"])
def get_writing_tasks():
    return jsonify(writing_tasks)

@bp.route("/submit", methods=["POST"])
def submit_writing():
    data = request.json
    # Here you could save responses to PostgreSQL and run AI evaluation
    return jsonify({
        "message": "Writing submission received",
        "task_id": data.get("task_id"),
        "response": data.get("response")
    })
