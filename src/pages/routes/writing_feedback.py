from flask import Blueprint, request, jsonify
import openai  # or another AI API client

bp = Blueprint("writing_feedback", __name__, url_prefix="/writing-feedback")

@bp.route("/evaluate", methods=["POST"])
def evaluate_writing():
    data = request.json
    essay = data.get("essay", "")

    # Example: call an AI model to evaluate essay
    # Replace with your chosen AI API (OpenAI, Azure OpenAI, etc.)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an IELTS examiner scoring essays."},
            {"role": "user", "content": f"Evaluate this IELTS essay:\n\n{essay}\n\nGive band score feedback for Task Response, Coherence & Cohesion, Lexical Resource, and Grammar."}
        ]
    )

    feedback = response["choices"][0]["message"]["content"]

    return jsonify({"feedback": feedback})
