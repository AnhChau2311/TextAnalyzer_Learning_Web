import json
import os
from flask import Blueprint, render_template, abort

scenario_bp = Blueprint("scenario", __name__)

DEFAULT_PATH = "scenarios/default_scenarios.json"
CUSTOM_PATH = "scenarios/custom_scenarios.json"

@scenario_bp.route("/scenario/<int:scenario_id>")
def show_scenario(scenario_id):
    scenarios = []

    # load default
    if os.path.exists(DEFAULT_PATH):
        with open(DEFAULT_PATH, encoding="utf-8") as f:
            scenarios.extend(json.load(f))

    # load custom
    if os.path.exists(CUSTOM_PATH):
        with open(CUSTOM_PATH, encoding="utf-8") as f:
            scenarios.extend(json.load(f))

    scenario = next((s for s in scenarios if s["id"] == scenario_id), None)

    if scenario is None:
        abort(404)

    return render_template("scenario.html", scenario=scenario)
