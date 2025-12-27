import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    ENV = os.getenv("FLASK_ENV", "production")

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
