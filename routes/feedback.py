"""
feedback.py - Route for processing and displaying feedback
"""

import json
import os
from flask import Blueprint, render_template, session, redirect, url_for

from logic.evaluator import evaluate_user_response
from logic.lesson_engine import get_personalized_lesson
from logic.hint_engine import get_smart_hint

feedback_bp = Blueprint("feedback", __name__)

DEFAULT_PATH = "scenarios/default_scenarios.json"
CUSTOM_PATH = "scenarios/custom_scenarios.json"


@feedback_bp.route("/feedback/<int:scenario_id>")
def show_feedback(scenario_id):

    scenarios = []

    # ================= LOAD SCENARIOS =================
    if os.path.exists(DEFAULT_PATH):
        with open(DEFAULT_PATH, encoding="utf-8") as f:
            scenarios.extend(json.load(f))

    if os.path.exists(CUSTOM_PATH):
        with open(CUSTOM_PATH, encoding="utf-8") as f:
            scenarios.extend(json.load(f))

    scenario = next((s for s in scenarios if s["id"] == scenario_id), None)

    if not scenario:
        return "Scenario not found", 404

    # ================= USER DATA =================
    answer = session.get("last_answer", "").strip()
    attempts = session.get(f"attempts_{scenario_id}", 0)

    if not answer:
        return redirect(
            url_for("scenario.show_scenario", scenario_id=scenario_id)
        )

    # ================= STEP 1: EVALUATION =================
    evaluation = evaluate_user_response(answer, scenario)

    # ================= STEP 2: LESSON =================
    lesson_data = get_personalized_lesson(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    # ================= STEP 3: HINT =================
    hint_data = get_smart_hint(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    # ================= SCORE & STYLE =================
    score = evaluation.get("overall_score", 0)
    style = evaluation.get("style", "neutral")

    style_map = {
        "very_polite": "Very polite 🌟",
        "polite": "Polite 😊",
        "neutral": "Neutral 😐",
        "needs_improvement": "Needs improvement 🌱",
        "harsh": "A bit harsh 😕"
    }

    # ================= RENDER =================
    return render_template(
        "feedback.html",

        # Core
        scenario=scenario,
        answer=answer,
        score=score,
        style_text=style_map.get(style, "Neutral"),

        # Analyzer outputs
        strengths=evaluation.get("strengths", []),
        weaknesses=evaluation.get("weaknesses", []),

        # ⭐ NEW: pass FULL analysis for score breakdown UI
        analysis=evaluation.get("analysis", {}),

        # Feedback & example
        feedback=evaluation.get("feedback", {}),
        improvement_example=evaluation.get("improvement_example"),

        # Lesson & hints
        lesson_data=lesson_data,
        hint_data=hint_data,

        # Misc
        highlighted_words=evaluation.get("highlighted_words", []),
        attempts=attempts,

        # Backward compatibility
        detailed_scores=evaluation.get("detailed_scores", {})
    )
