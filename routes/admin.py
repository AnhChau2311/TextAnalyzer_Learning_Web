import json
import os
from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/create", methods=["GET", "POST"])
def create_scenario():
    if request.method == "POST":
        new_scenario = {
            "id": None,
            "title": request.form["title"],
            "story": request.form["story"],
            "question": request.form["question"],
            "goal": request.form["goal"]
        }

        file_path = "scenarios/custom_scenarios.json"

        # ✅ SAFE LOAD
        if not os.path.exists(file_path):
            scenarios = []
        else:
            try:
                with open(file_path, encoding="utf-8") as f:
                    scenarios = json.load(f)
            except json.JSONDecodeError:
                scenarios = []

        new_scenario["id"] = len(scenarios) + 100
        scenarios.append(new_scenario)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(scenarios, f, indent=2, ensure_ascii=False)

        return redirect(url_for("home.home"))

    return render_template("admin_create.html")

@admin_bp.route("/admin/delete/<int:scenario_id>", methods=["POST"])
def delete_scenario(scenario_id):
    file_path = "scenarios/custom_scenarios.json"

    if not os.path.exists(file_path):
        return redirect(url_for("home.home"))

    try:
        with open(file_path, encoding="utf-8") as f:
            scenarios = json.load(f)
    except json.JSONDecodeError:
        scenarios = []

    scenarios = [s for s in scenarios if s["id"] != scenario_id]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(scenarios, f, indent=2, ensure_ascii=False)

    return redirect(url_for("home.home"))
