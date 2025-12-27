from flask import Blueprint, request, redirect, url_for, session

answer_bp = Blueprint("answer", __name__)


@answer_bp.route("/answer/<int:scenario_id>", methods=["POST"])
def submit_answer(scenario_id):
    """
    Handle the submission of a child's answer.

    Responsibilities:
    1. Validate input
    2. Store the answer in session
    3. Track the number of attempts per scenario
    4. Redirect to feedback page
    """
    user_answer = request.form.get("answer", "").strip()

    # If the answer is empty, return to the scenario page
    if not user_answer:
        return redirect(
            url_for("scenario.show_scenario", scenario_id=scenario_id)
        )

    # Store the latest answer (used by feedback route)
    session["last_answer"] = user_answer

    # Track attempts for this scenario
    attempts_key = f"attempts_{scenario_id}"
    session[attempts_key] = session.get(attempts_key, 0) + 1

    return redirect(
        url_for("feedback.show_feedback", scenario_id=scenario_id)
    )
