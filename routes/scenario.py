import json
from flask import Blueprint, render_template, abort

scenario_bp = Blueprint("scenario", __name__)

@scenario_bp.route("/scenario/<int:scenario_id>")
def show_scenario(scenario_id):
    with open("scenarios/default_scenarios.json", encoding="utf-8") as f:
        scenarios = json.load(f)

    scenario = next((s for s in scenarios if s["id"] == scenario_id), None)

    if scenario is None:
        abort(404)

    return render_template("scenario.html", scenario=scenario)
