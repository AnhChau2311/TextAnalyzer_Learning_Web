from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import blueprints
    from routes.home import home_bp
    from routes.scenario import scenario_bp
    from routes.answer import answer_bp
    from routes.admin import admin_bp
    from routes.feedback import feedback_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(scenario_bp)
    app.register_blueprint(answer_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(feedback_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
