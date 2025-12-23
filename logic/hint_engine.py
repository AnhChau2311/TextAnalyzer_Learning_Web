"""
hint_engine.py - Generate flexible improvement hints
based on the child's actual response.
"""

import os
import random
from openai import OpenAI

client = OpenAI()


class HintEngine:
    """
    Engine for generating adaptive hints to improve a child's response.
    """

    def __init__(self):
        self.client = client

    def generate_hint(
        self,
        user_answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Generate an improvement hint based on the real response.

        Args:
            user_answer: The child's answer
            scenario: Scenario dictionary
            evaluation: Evaluation result

        Returns:
            A concrete, child-friendly hint
        """
        if evaluation["overall_score"] >= 80:
            return self._generate_encouragement_hint(
                user_answer, scenario
            )

        return self._generate_improvement_hint(
            user_answer, scenario, evaluation
        )

    def _generate_encouragement_hint(
        self,
        answer: str,
        scenario: dict
    ) -> str:
        """
        Generate a short encouragement when the answer is already good.
        """
        prompt = f"""
A student has answered very well in the following situation:

SITUATION: {scenario['title']}
STUDENT'S ANSWER: "{answer}"

Write a short encouragement (1–2 sentences) to motivate the student.
You may gently suggest one small improvement to make the answer even better.

Use a friendly teacher-like tone.
DO NOT use bullet points or markdown formatting.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a supportive teacher who encourages students."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=150
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error generating encouragement hint: {e}")
            return (
                "Great job! Your answer is kind and polite. "
                "Keep using this friendly communication style!"
            )

    def _generate_improvement_hint(
        self,
        answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Generate a concrete improvement hint based on the response.
        """
        ai_areas = evaluation["ai_evaluation"].get(
            "areas_for_improvement", []
        )
        antlr_suggestions = evaluation["antlr_analysis"].get(
            "suggestions", []
        )

        all_improvements = ai_areas + antlr_suggestions

        prompt = f"""
A student is learning communication skills:

SITUATION: {scenario['title']}
STORY: {scenario['story']}
GOAL: {scenario['goal']}

STUDENT'S ANSWER: "{answer}"

AREAS TO IMPROVE:
{chr(10).join(f"- {item}" for item in all_improvements[:3])}

Write a concrete hint (2–3 sentences) to help the student improve.
The hint should:
1. Start by acknowledging something the student did well
2. Give a SPECIFIC example of a better way to say it (you may write a sample sentence)
3. Explain WHY that way is better

Use simple, friendly language.
DO NOT use bullet points or markdown formatting.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a patient teacher who explains things clearly."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=250
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error generating improvement hint: {e}")
            return (
                "You can try adding a greeting and saying thank you "
                "to make your sentence sound more polite."
            )

    def generate_alternative_response(
        self,
        scenario: dict,
        user_answer: str
    ) -> str:
        """
        Generate a model answer inspired by the student's response.
        """
        prompt = f"""
A student is learning how to {scenario['goal']}.

SITUATION: {scenario['title']}
STORY: {scenario['story']}

STUDENT'S ANSWER: "{user_answer}"

Write a BETTER model answer for this situation.
The model answer should:
- Keep part of the student's original idea
- Add polite elements such as greetings, thanks, or apologies (if appropriate)
- Use gentle and kind words
- Be suitable for primary school children

ONLY write the model answer.
DO NOT explain anything.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a teacher skilled at writing model answers."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=100
            )

            return response.choices[0].message.content.strip().strip('"')

        except Exception as e:
            print(f"Error generating alternative response: {e}")
            return None


def get_smart_hint(
    user_answer: str,
    scenario: dict,
    evaluation: dict
) -> dict:
    """
    Retrieve a smart hint package.

    Returns:
        {
            "hint_text": "...",
            "alternative_response": "...",
            "tip": "..."
        }
    """
    engine = HintEngine()

    hint_text = engine.generate_hint(
        user_answer, scenario, evaluation
    )

    alternative = None
    if evaluation["overall_score"] < 60:
        alternative = engine.generate_alternative_response(
            scenario, user_answer
        )

    tip = _get_goal_specific_tip(
        scenario["goal"], evaluation
    )

    return {
        "hint_text": hint_text,
        "alternative_response": alternative,
        "tip": tip
    }


def _get_goal_specific_tip(goal: str, evaluation: dict) -> str:
    """
    Return a short tip based on the learning goal
    and missing language elements.
    """
    has_greeting = evaluation["antlr_analysis"].get("has_greeting", False)
    has_thank_you = evaluation["antlr_analysis"].get("has_thank_you", False)
    has_apology = evaluation["antlr_analysis"].get("has_apology", False)
    has_softening = evaluation["antlr_analysis"].get("has_softening", False)

    tips_map = {
        "giving_feedback": [
            "💡 Start your opinion with 'I think...' or 'Maybe...' to sound gentler.",
            "💡 Using 'could' instead of 'should' feels kinder!",
            "💡 Praising first makes feedback easier to accept."
        ],
        "polite_refusal": [
            "💡 When refusing, try thanking the person first!",
            "💡 Explaining your reason helps others understand.",
            "💡 You can suggest another time: 'Maybe next time?'"
        ],
        "apologizing": [
            "💡 A sincere apology clearly says what you are sorry for.",
            "💡 Showing understanding helps others feel better.",
            "💡 Promising to improve is a strong part of an apology."
        ],
        "asking_for_help": [
            "💡 Starting with 'Could you please...' sounds very polite!",
            "💡 Explain why you need help.",
            "💡 Ending with 'Thank you!' is always a good idea."
        ]
    }

    goal_tips = tips_map.get(goal, [
        "💡 Greetings and thank-yous make sentences kinder.",
        "💡 Use 'please' when asking for something.",
        "💡 Gentle words make communication better."
    ])

    if goal == "apologizing" and not has_apology:
        return "💡 Don’t forget to say 'I'm sorry' when apologizing."

    if goal == "asking_for_help":
        if not has_thank_you:
            return "💡 Ending with 'Thank you!' makes your request polite."
        if not has_softening:
            return "💡 Try 'Could you please...' instead of 'Can you...'."

    return random.choice(goal_tips)
