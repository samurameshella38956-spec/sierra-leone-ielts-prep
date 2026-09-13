from flask import Blueprint, jsonify

bp = Blueprint("scholarship", __name__, url_prefix="/scholarship")

scholarships = [
    {
        "id": 1,
        "title": "Erasmus Mundus Joint Masters",
        "deadline": "2026-12-01",
        "eligibility": "Open to all international students",
        "link": "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus"
    },
    {
        "id": 2,
        "title": "Commonwealth Master's Scholarships (UK)",
        "deadline": "2026-12-15",
        "eligibility": "Students from Commonwealth countries",
        "link": "https://cscuk.fcdo.gov.uk/scholarships/"
    },
    {
        "id": 3,
        "title": "Open Doors Russian Scholarship",
        "deadline": "2027-01-10",
        "eligibility": "International students in STEM, Medicine, Economics",
        "link": "https://od.globaluni.ru/"
    }
]

@bp.route("/updates", methods=["GET"])
def get_scholarship_updates():
    return jsonify(scholarships)
