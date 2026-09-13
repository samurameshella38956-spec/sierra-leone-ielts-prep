from flask import Blueprint, request, jsonify

bp = Blueprint("payment", __name__, url_prefix="/payment")

# Example: store subscription status in DB
subscriptions = {}

@bp.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    user_id = data.get("user_id")
    method = data.get("method")  # "OrangeMoney" or "Afrimoney"

    # Normally: integrate with Orange Money / Afrimoney APIs here
    # For now, simulate success
    subscriptions[user_id] = {"status": "active", "method": method}
    return jsonify({"message": "Subscription activated", "plan": "Premium", "method": method})

@bp.route("/status/<user_id>", methods=["GET"])
def check_status(user_id):
    status = subscriptions.get(user_id, {"status": "inactive"})
    return jsonify(status)
