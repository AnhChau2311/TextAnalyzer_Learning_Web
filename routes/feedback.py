"""
feedback.py - Route for processing and displaying feedback
"""

import json
from flask import Blueprint, render_template, session, redirect, url_for

from logic.evaluator import evaluate_user_response
from logic.lesson_engine import get_personalized_lesson
from logic.hint_engine import get_smart_hint

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/feedback/<int:scenario_id>")
def show_feedback(scenario_id):
    """
    Display feedback after a child submits an answer.

    Flow:
    1. Load scenario
    2. Retrieve answer from session
    3. Evaluate the answer (ANTLR-based core analysis)
    4. Generate a personalized lesson
    5. Generate improvement hints
    6. Render the feedback template
    """

    # ===== Load scenario =====
    with open("scenarios/default_scenarios.json", encoding="utf-8") as f:
        scenarios = json.load(f)

    scenario = next(
        (s for s in scenarios if s["id"] == scenario_id),
        None
    )

    if not scenario:
        return "Scenario not found", 404

    # ===== Retrieve user data =====
    answer = session.get("last_answer", "").strip()
    attempts = session.get(f"attempts_{scenario_id}", 0)

    if not answer:
        return redirect(
            url_for("scenario.show_scenario", scenario_id=scenario_id)
        )

    # ===== STEP 1: Core evaluation (ANTLR-based) =====
    evaluation = evaluate_user_response(answer, scenario)

    # ===== STEP 2: Generate personalized lesson =====
    lesson_data = get_personalized_lesson(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    # ===== STEP 3: Generate improvement hints =====
    hint_data = get_smart_hint(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    # ===== STEP 4: Prepare data for template =====
    score = evaluation["overall_score"]
    style = evaluation["style"]

    # Map internal style to user-friendly text
    style_map = {
        "very_polite": "Very polite 🌟",
        "polite": "Polite 😊",
        "neutral": "Neutral 😐",
        "harsh": "A bit harsh 😕",
        "needs_improvement": "Needs improvement 🌱"
    }
    style_text = style_map.get(style, "Neutral")

    # ===== Render template =====
    return render_template(
        "feedback.html",
        scenario=scenario,
        answer=answer,
        score=score,
        style_text=style_text,
        strengths=evaluation.get("strengths", []),
        weaknesses=evaluation.get("weaknesses", []),
        feedback=evaluation["feedback"],
        improvement_example=evaluation.get("improvement_example"),
        lesson_data=lesson_data,
        hint_data=hint_data,
        highlighted_words=evaluation.get("highlighted_words", []),
        attempts=attempts,
        detailed_scores=evaluation.get("detailed_scores", {})
    )
