"""
lesson_engine.py - Generate personalized lessons for children
"""

import random


class LessonEngine:
    """
    Engine for generating personalized lessons
    suitable for children aged 6–10.
    """

    def __init__(self):
        # Lessons grouped by communication goal
        self.lessons = {
            "giving_feedback": {
                "title": "💬 Giving Kind Feedback",
                "principle": (
                    "Giving feedback helps others improve, "
                    "not to criticize them!"
                ),
                "steps": [
                    "1️⃣ Say something good first",
                    "2️⃣ Use gentle words (I think, maybe...)",
                    "3️⃣ Give suggestions instead of blaming",
                    "4️⃣ Encourage and show trust"
                ],
                "examples": {
                    "bad":
                        "❌ \"That drawing is terrible! Everything is wrong!\"",
                    "good":
                        "✅ \"Your picture has nice colors! "
                        "I think adding more details could make it even better!\""
                }
            },
            "polite_refusal": {
                "title": "🤝 Polite Refusal",
                "principle": (
                    "A polite refusal helps keep friendships "
                    "and avoids hurting others."
                ),
                "steps": [
                    "1️⃣ Say thank you",
                    "2️⃣ Explain the reason",
                    "3️⃣ Show regret",
                    "4️⃣ Suggest another time"
                ],
                "examples": {
                    "bad":
                        "❌ \"No! I don’t want to play!\"",
                    "good":
                        "✅ \"Thank you for inviting me! "
                        "I’m very tired today. "
                        "Maybe we can play together tomorrow?\""
                }
            },
            "apologizing": {
                "title": "🙏 Sincere Apology",
                "principle": (
                    "A good apology means taking responsibility, "
                    "showing empathy, and promising to improve."
                ),
                "steps": [
                    "1️⃣ Say sorry clearly",
                    "2️⃣ Explain what you are sorry for",
                    "3️⃣ Show you understand the other person’s feelings",
                    "4️⃣ Promise to be more careful"
                ],
                "examples": {
                    "bad":
                        "❌ \"Sorry.\" (too short and not sincere)",
                    "good":
                        "✅ \"I’m sorry for losing your pencil. "
                        "I know it was important to you. "
                        "I will be more careful next time!\""
                }
            },
            "asking_for_help": {
                "title": "🆘 Asking for Help Politely",
                "principle": (
                    "Asking politely makes others happy to help you!"
                ),
                "steps": [
                    "1️⃣ Greet the person",
                    "2️⃣ Use 'Could you...' or 'Please...'",
                    "3️⃣ Say clearly what you need help with",
                    "4️⃣ Say thank you"
                ],
                "examples": {
                    "bad":
                        "❌ \"Solve this for me!\"",
                    "good":
                        "✅ \"Hello! Could you please help me "
                        "solve this problem? I’m a bit stuck. "
                        "Thank you very much!\""
                }
            }
        }

        # Key principles for each goal
        self.key_principles = {
            "giving_feedback":
                "🎯 Feedback = Praise + Suggestion + Encouragement",
            "polite_refusal":
                "🤝 Refusal = Thank you + Reason + Alternative",
            "apologizing":
                "🙏 Apology = Responsibility + Empathy + Promise",
            "asking_for_help":
                "🆘 Asking for help = Greeting + Politeness + Clarity + Thanks"
        }

    def generate_lesson(
        self,
        user_answer: str,
        scenario: dict,
        evaluation: dict
    ) -> dict:
        """
        Generate a personalized lesson based on evaluation results.

        Returns:
            {
                "lesson_text": str,
                "key_principle": str,
                "practice_tips": list,
                "examples": dict
            }
        """

        goal = scenario["goal"]
        score = evaluation["overall_score"]
        strengths = evaluation.get("strengths", [])
        weaknesses = evaluation.get("weaknesses", [])

        lesson_data = self.lessons.get(
            goal,
            self._get_default_lesson()
        )

        if score >= 80:
            lesson_text = self._create_excellence_lesson(
                lesson_data,
                strengths
            )
        elif score >= 60:
            lesson_text = self._create_improvement_lesson(
                lesson_data,
                weaknesses
            )
        else:
            lesson_text = self._create_foundation_lesson(
                lesson_data
            )

        practice_tips = self._get_practice_tips(goal)

        return {
            "lesson_text": lesson_text,
            "key_principle": self.key_principles.get(
                goal,
                "💡 Good communication = Respect + Politeness + Sincerity"
            ),
            "practice_tips": practice_tips,
            "examples": lesson_data["examples"]
        }

    def _create_excellence_lesson(
        self,
        lesson_data: dict,
        strengths: list
    ) -> str:
        """Lesson for strong performance."""

        lesson = (
            f"🌟 **Excellent!** You understand "
            f"{lesson_data['title']} very well!\n\n"
        )

        if strengths:
            lesson += "**Your strengths:**\n"
            for strength in strengths[:3]:
                lesson += f"✅ {strength}\n"
            lesson += "\n"

        lesson += (
            f"**Remember:** {lesson_data['principle']}\n\n"
            "Keep using this way of speaking. "
            "You are a great example for others! 🎯"
        )

        return lesson

    def _create_improvement_lesson(
        self,
        lesson_data: dict,
        weaknesses: list
    ) -> str:
        """Lesson for partial understanding."""

        lesson = (
            f"💪 **Good effort!** You are learning "
            f"{lesson_data['title']}.\n\n"
        )

        lesson += (
            f"**Important principle:** "
            f"{lesson_data['principle']}\n\n"
        )

        if weaknesses:
            lesson += "**What to improve:**\n"
            for i, weakness in enumerate(weaknesses[:2], 1):
                lesson += f"{i}. {weakness}\n"
            lesson += "\n"

        lesson += "**Compare:**\n"
        lesson += f"{lesson_data['examples']['bad']}\n"
        lesson += f"{lesson_data['examples']['good']}\n\n"

        lesson += (
            "Try again and apply these ideas. 🌱"
        )

        return lesson

    def _create_foundation_lesson(
        self,
        lesson_data: dict
    ) -> str:
        """Lesson for beginners."""

        lesson = (
            f"🌱 **Let’s start from the basics:** "
            f"{lesson_data['title']}\n\n"
        )

        lesson += (
            f"**Why is it important?** "
            f"{lesson_data['principle']}\n\n"
        )

        lesson += "**Steps to follow:**\n"
        for step in lesson_data["steps"]:
            lesson += f"{step}\n"
        lesson += "\n"

        lesson += "**Learn from examples:**\n"
        lesson += (
            f"{lesson_data['examples']['bad']} "
            "→ This can hurt others\n"
        )
        lesson += (
            f"{lesson_data['examples']['good']} "
            "→ This is much better!\n\n"
        )

        lesson += (
            "Don’t worry! Everyone learns step by step. "
            "Give it another try! 💪"
        )

        return lesson

    def _get_practice_tips(self, goal: str) -> list:
        """Return practice tips for the goal."""

        tips = {
            "giving_feedback": [
                "📝 Practice: Praise one thing + suggest one improvement",
                "🎮 Role-play: Give feedback on a drawing",
                "👥 Practice with parents: Comment on a meal"
            ],
            "polite_refusal": [
                "📝 Practice: Refuse an invitation politely",
                "🎮 Role-play: Practice saying no kindly",
                "👥 Practice with friends: Invite and refuse gently"
            ],
            "apologizing": [
                "📝 Practice: Write a short apology note",
                "🎮 Scenario: What if you break a friend’s item?",
                "👥 Practice at home: Apologize for forgetting chores"
            ],
            "asking_for_help": [
                "📝 Practice: Ask for help with homework",
                "🎮 Scenario: Ask for help in a game",
                "👥 Practice: Ask parents for small help"
            ]
        }

        return tips.get(
            goal,
            ["💡 Practice every day to improve!"]
        )

    def _get_default_lesson(self) -> dict:
        """Default lesson if goal is unknown."""

        return {
            "title": "💬 Good Communication",
            "principle":
                "Speaking politely helps people like and respect you!",
            "steps": [
                "1️⃣ Always greet others",
                "2️⃣ Say thank you and sorry",
                "3️⃣ Use gentle words",
                "4️⃣ Listen to others"
            ],
            "examples": {
                "bad":
                    "❌ \"No! I don’t like it!\"",
                "good":
                    "✅ \"I’m sorry, I can’t do that. Thank you anyway!\""
            }
        }


def get_personalized_lesson(
    user_answer: str,
    scenario: dict,
    evaluation: dict
) -> dict:
    """
    Compatibility wrapper for existing code.
    """

    engine = LessonEngine()
    return engine.generate_lesson(user_answer, scenario, evaluation)
