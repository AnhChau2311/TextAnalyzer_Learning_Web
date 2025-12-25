"""
hint_engine.py - Generate smart improvement hints for children
Templates are prioritized; AI is used only when necessary.
"""

import random
from openai import OpenAI

client = OpenAI()


class HintEngine:
    """
    Engine for generating improvement hints
    in a child-friendly and educational way.
    """

    def __init__(self):
        self.client = client

        # Hint templates grouped by communication goal
        self.hint_templates = {
            "giving_feedback": {
                "missing_softening": [
                    "💡 Try adding 'I think...' or 'Maybe...' before giving feedback!",
                    "💡 Using 'You could try...' sounds gentler.",
                    "💡 Starting with 'In my opinion...' makes it easier to hear."
                ],
                "has_strong_words": [
                    "💡 Instead of 'wrong', try 'maybe we can do it another way?'",
                    "💡 Say 'not very good yet' instead of 'bad'.",
                    "💡 'Not suitable yet' sounds kinder than 'incorrect'."
                ],
                "missing_positive": [
                    "💡 Try saying something good before giving feedback!",
                    "💡 Start with 'I like this, but...' to sound nicer.",
                    "💡 Praising first helps others listen better."
                ]
            },
            "polite_refusal": {
                "missing_thank": [
                    "💡 Try thanking the invitation before refusing.",
                    "💡 'Thank you for inviting me, but...' sounds polite.",
                    "💡 Starting with 'Thanks!' helps keep friendships."
                ],
                "missing_reason": [
                    "💡 Explaining the reason helps others understand.",
                    "💡 Adding 'because...' makes your refusal clearer.",
                    "💡 A reason avoids misunderstandings."
                ],
                "missing_alternative": [
                    "💡 Suggest another time: 'Maybe next time!'",
                    "💡 'How about another day?' shows you still care.",
                    "💡 Offering an alternative softens a refusal."
                ]
            },
            "apologizing": {
                "missing_apology": [
                    "💡 Don’t forget to say 'I’m sorry'!",
                    "💡 A sincere apology is the first step to fixing things.",
                    "💡 'I’m sorry' is short but very important."
                ],
                "missing_empathy": [
                    "💡 Try adding 'I understand you feel sad.'",
                    "💡 'I know that hurt you' shows understanding.",
                    "💡 Showing empathy helps others feel better."
                ],
                "missing_promise": [
                    "💡 Promise to improve: 'I will be more careful next time.'",
                    "💡 'I’ll try to do better' makes your apology stronger.",
                    "💡 A promise shows you really want to change."
                ]
            },
            "asking_for_help": {
                "missing_polite_verb": [
                    "💡 Use 'Could you...' or 'Can you help me?'",
                    "💡 'Please help me...' sounds polite.",
                    "💡 'Could you please...' is better than giving orders."
                ],
                "missing_thank": [
                    "💡 Ending with 'Thank you!' is very polite.",
                    "💡 'Thanks!' is short but important.",
                    "💡 People feel happy when they hear 'thank you'."
                ],
                "unclear_request": [
                    "💡 Say clearly what you need help with.",
                    "💡 'I need help with...' makes it clearer.",
                    "💡 Clear requests get better help."
                ]
            }
        }

    def generate_hint(
        self,
        user_answer: str,
        scenario: dict,
        evaluation: dict
    ) -> dict:
        """
        Generate a complete hint package.

        Returns:
            {
                "hint_text": str,
                "tips": list,
                "example_phrases": list
            }
        """

        score = evaluation["overall_score"]
        goal = scenario["goal"]
        weaknesses = evaluation.get("weaknesses", [])

        if score >= 85:
            return self._generate_excellence_hint(goal)

        hint_text = self._select_hint_from_template(goal, weaknesses)
        tips = self._get_goal_tips(goal)
        example_phrases = self._get_example_phrases(goal)

        return {
            "hint_text": hint_text,
            "tips": tips,
            "example_phrases": example_phrases
        }

    def _generate_excellence_hint(self, goal: str) -> dict:
        """Hint for excellent responses."""

        excellence_messages = {
            "giving_feedback":
                "🌟 Excellent! Your feedback is kind and thoughtful.",
            "polite_refusal":
                "🌟 Perfect! Your refusal is very polite and respectful.",
            "apologizing":
                "🌟 Great job! Your apology sounds sincere.",
            "asking_for_help":
                "🌟 Well done! You asked for help very politely."
        }

        return {
            "hint_text": excellence_messages.get(
                goal,
                "🌟 Excellent! Your sentence is very good."
            ),
            "tips": [
                "⭐ Remember this way of speaking and use it again!"
            ],
            "example_phrases": []
        }

    def _select_hint_from_template(
        self,
        goal: str,
        weaknesses: list
    ) -> str:
        """Select the most relevant hint based on weaknesses."""

        if goal not in self.hint_templates:
            return (
                "💡 Try adding a greeting and a thank-you "
                "to sound more polite."
            )

        templates = self.hint_templates[goal]

        for weakness in weaknesses:
            if "Missing a greeting" in weakness and "missing_greeting" in templates:
                return random.choice(templates["missing_greeting"])
            if "Missing a thank-you" in weakness and "missing_thank" in templates:
                return random.choice(templates["missing_thank"])
            if "Uses strong or harsh words" in weakness and "has_strong_words" in templates:
                return random.choice(templates["has_strong_words"])
            if "Sounds too commanding" in weakness and "missing_polite_verb" in templates:
                return random.choice(templates["missing_polite_verb"])
            if "Missing an apology" in weakness and "missing_apology" in templates:
                return random.choice(templates["missing_apology"])
            if "Missing softening words" in weakness and "missing_softening" in templates:
                return random.choice(templates["missing_softening"])

        first_key = list(templates.keys())[0]
        return random.choice(templates[first_key])

    def _get_goal_tips(self, goal: str) -> list:
        """Return short tips based on the communication goal."""

        tips_map = {
            "giving_feedback": [
                "🎯 Formula: Praise + Suggestion + Encouragement",
                "🎯 Use 'I think...' instead of blaming",
                "🎯 Focus on solutions, not mistakes"
            ],
            "polite_refusal": [
                "🎯 Formula: Thank + Reason + Alternative",
                "🎯 Explain your reason clearly",
                "🎯 Suggest another time"
            ],
            "apologizing": [
                "🎯 Formula: Apology + Empathy + Promise",
                "🎯 Say clearly what you are sorry for",
                "🎯 Show you understand the other person"
            ],
            "asking_for_help": [
                "🎯 Formula: Greeting + Polite request + Thank you",
                "🎯 Use 'Could you...' instead of commands",
                "🎯 Explain what help you need"
            ]
        }

        return tips_map.get(
            goal,
            ["💡 Greetings and thank-yous are always helpful."]
        )[:2]

    def _get_example_phrases(self, goal: str) -> list:
        """Return example phrases for the goal."""

        phrases_map = {
            "giving_feedback": [
                "I think maybe...",
                "You could try...",
                "In my opinion...",
                "Perhaps we can..."
            ],
            "polite_refusal": [
                "Thank you for inviting me, but...",
                "I would love to, but...",
                "Maybe another day!",
                "How about next time?"
            ],
            "apologizing": [
                "I’m sorry about...",
                "I didn’t mean to...",
                "I understand you feel...",
                "I will try to..."
            ],
            "asking_for_help": [
                "Could you help me?",
                "Please help me...",
                "I need help with...",
                "Thank you very much!"
            ]
        }

        return phrases_map.get(goal, [])[:3]


def get_smart_hint(
    user_answer: str,
    scenario: dict,
    evaluation: dict
) -> dict:
    """
    Compatibility wrapper for existing code.
    """
    engine = HintEngine()
    return engine.generate_hint(user_answer, scenario, evaluation)
