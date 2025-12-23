import json
import os
from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)

DEFAULT_PATH = "scenarios/default_scenarios.json"
CUSTOM_PATH = "scenarios/custom_scenarios.json"


@home_bp.route("/")
def home():
    with open(DEFAULT_PATH, encoding="utf-8") as f:
        default_scenarios = json.load(f)

    if os.path.exists(CUSTOM_PATH):
        try:
            with open(CUSTOM_PATH, encoding="utf-8") as f:
                custom_scenarios = json.load(f)
        except json.JSONDecodeError:
            custom_scenarios = []
    else:
        custom_scenarios = []

    return render_template(
        "index.html",
        default_scenarios=default_scenarios,
        custom_scenarios=custom_scenarios
    )
