import json
from flask import Blueprint, render_template, session

from analysis.analyzer import analyze_sentence
from logic.evaluator import evaluate_user_response
from logic.lesson_engine import get_personalized_lesson
from logic.hint_engine import get_smart_hint

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/feedback/<int:scenario_id>")
def show_feedback(scenario_id):
    # ===== Load scenarios =====
    with open("scenarios/default_scenarios.json", encoding="utf-8") as f:
        scenarios = json.load(f)

    scenario = next((s for s in scenarios if s["id"] == scenario_id), None)

    if not scenario:
        return "Scenario not found", 404

    # ===== Get user data from session =====
    answer = session.get("last_answer", "").strip()
    attempts = session.get(f"attempts_{scenario_id}", 0)

    if not answer:
        return "No answer found", 400

    # ===== STEP 1: Basic ANTLR analysis =====
    antlr_analysis = analyze_sentence(answer)

    # ===== STEP 2: Full evaluation (ANTLR + AI) =====
    evaluation = evaluate_user_response(answer, scenario)

    score = evaluation["overall_score"]

    # ===== STEP 3: Lesson generation =====
    lesson_data = get_personalized_lesson(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    lesson_text = lesson_data["lesson_text"]
    key_principle = lesson_data["key_principle"]

    # ===== STEP 4: Hint generation (adaptive) =====
    hint_data = get_smart_hint(
        user_answer=answer,
        scenario=scenario,
        evaluation=evaluation
    )

    hint_text = hint_data["hint_text"]
    alternative_response = hint_data["alternative_response"]
    tip = hint_data["tip"]

    # ===== STEP 5: Friendly feedback summary (UI-level) =====
    if score >= 80:
        feedback_summary = "🌟 Great job! Your words sound kind and respectful."
    elif score >= 60:
        feedback_summary = "😊 Nice try! Your answer is good, and it can be even better."
    else:
        feedback_summary = (
            "🌱 It's okay — learning takes time. Let's see how we can improve this together."
        )

    return render_template(
        "feedback.html",
        scenario=scenario,
        answer=answer,
        score=score,
        feedback_summary=feedback_summary,
        lesson_text=lesson_text,
        key_principle=key_principle,
        hint_text=hint_text,
        alternative_response=alternative_response,
        tip=tip,
        attempts=attempts,
        antlr_analysis=antlr_analysis,
        highlighted_words=evaluation.get("highlighted_words", [])
    )
