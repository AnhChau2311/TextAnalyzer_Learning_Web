"""
lesson_engine.py - Generate personalized lessons based on the story
and the child's response.
"""

import os
from openai import OpenAI

client = OpenAI()

class LessonEngine:
    """
    Engine for generating personalized, educational lessons
    for children based on their answers.
    """

    def __init__(self):
        self.client = client

    def generate_lesson(
        self,
        user_answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Generate a lesson adapted to the child's response.

        Args:
            user_answer: The child's answer
            scenario: Scenario dictionary
            evaluation: Evaluation result

        Returns:
            A personalized lesson text
        """
        lesson_type = self._determine_lesson_type(evaluation)

        if lesson_type == "positive_reinforcement":
            return self._generate_positive_lesson(
                user_answer, scenario, evaluation
            )
        elif lesson_type == "gentle_correction":
            return self._generate_corrective_lesson(
                user_answer, scenario, evaluation
            )
        else:
            return self._generate_balanced_lesson(
                user_answer, scenario, evaluation
            )

    def _determine_lesson_type(self, evaluation: dict) -> str:
        """
        Determine which type of lesson should be generated.
        """
        score = evaluation["overall_score"]

        if score >= 80:
            return "positive_reinforcement"
        elif score >= 50:
            return "balanced"
        else:
            return "gentle_correction"

    def _generate_positive_lesson(
        self,
        answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Lesson for strong answers – focuses on reinforcement
        and generalization.
        """
        strengths = evaluation["ai_evaluation"].get("strengths", [])

        prompt = f"""
A student has given a VERY GOOD answer to the following situation:

SITUATION: {scenario['title']}
GOAL: {scenario['goal']}
ANSWER: "{answer}"

STRENGTHS:
{chr(10).join(f"- {s}" for s in strengths)}

Write a short lesson (2–3 sentences) that:
1. Explains WHY this answer is good
2. Encourages using this communication style in similar situations
3. States a general principle the student can remember

Use an encouraging and positive tone.
DO NOT use bullet points or markdown formatting.
Start with an emoji 🌟 or ✨
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a teacher who encourages and motivates students."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error generating positive lesson: {e}")
            return (
                "🌟 Great job! Your words are polite and thoughtful. "
                "Remember that speaking kindly helps build good relationships "
                "in every conversation."
            )

    def _generate_corrective_lesson(
        self,
        answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Lesson for answers that need improvement – focuses on learning.
        """
        improvements = evaluation["ai_evaluation"].get(
            "areas_for_improvement", []
        )
        goal = scenario["goal"]

        prompt = f"""
A student is learning the communication skill: {goal}

SITUATION: {scenario['title']}
STUDENT'S ANSWER: "{answer}"

AREAS TO IMPROVE:
{chr(10).join(f"- {i}" for i in improvements[:2])}

Write a short lesson (3–4 sentences) that:
1. Explains an important communication principle for this situation
2. Compares an unkind way of speaking vs. a polite way
3. Encourages the student to try again with a positive mindset

Use a supportive and understanding tone.
DO NOT criticize.
DO NOT use bullet points or markdown formatting.
Start with an emoji 🌱 or 💡
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a patient and encouraging teacher."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=250
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error generating corrective lesson: {e}")
            return (
                "🌱 Polite communication helps us get along with others. "
                "Try adding kind words like ‘please’ or ‘thank you’, and use a "
                "gentler tone. Give it another try—you can do it!"
            )

    def _generate_balanced_lesson(
        self,
        answer: str,
        scenario: dict,
        evaluation: dict
    ) -> str:
        """
        Balanced lesson – praises strengths and guides improvement.
        """
        strengths = evaluation["ai_evaluation"].get("strengths", [])
        improvements = evaluation["ai_evaluation"].get(
            "areas_for_improvement", []
        )

        prompt = f"""
A student is practicing communication skills:

SITUATION: {scenario['title']}
GOAL: {scenario['goal']}
ANSWER: "{answer}"

WHAT WAS DONE WELL:
{chr(10).join(f"- {s}" for s in strengths[:2])}

WHAT CAN BE IMPROVED:
{chr(10).join(f"- {i}" for i in improvements[:2])}

Write a short lesson (3 sentences) with this structure:
1. Praise what the student did well
2. Explain one improvement and why it matters
3. Encourage the student to try again

Use a balanced, friendly teaching tone.
DO NOT use bullet points or markdown formatting.
Start with an emoji 💫 or 🎯
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a teacher who balances praise and guidance."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error generating balanced lesson: {e}")
            return (
                "💫 You did some things well in your sentence! "
                "To make it even better, try adding polite words like "
                "‘please’ or ‘thank you’. Keep practicing!"
            )

    def generate_related_scenarios(
        self,
        scenario: dict,
        count: int = 3
    ) -> list:
        """
        Generate similar practice scenarios for further learning.
        """
        prompt = f"""
Create {count} new practice situations for children to learn the skill:
{scenario['goal']}

ORIGINAL SITUATION:
Title: {scenario['title']}
Story: {scenario['story']}

Create {count} DIFFERENT situations with the same learning goal.
Each situation should include:
- A short title (4–6 words)
- A short story (2–3 sentences, suitable for primary school children)

Return the result as a JSON array:
[
  {{
    "title": "...",
    "story": "..."
  }}
]
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a teacher who creates learning scenarios for children."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                response_format={"type": "json_object"}
            )

            import json
            result = json.loads(response.choices[0].message.content)
            return result.get("scenarios", [])

        except Exception as e:
            print(f"Error generating related scenarios: {e}")
            return []


def get_personalized_lesson(
    user_answer: str,
    scenario: dict,
    evaluation: dict
) -> dict:
    """
    Retrieve a personalized lesson package.

    Returns:
        {
            "lesson_text": "...",
            "key_principle": "...",
            "related_scenarios": [...]
        }
    """
    engine = LessonEngine()

    lesson_text = engine.generate_lesson(
        user_answer, scenario, evaluation
    )

    key_principle = _extract_key_principle(
        scenario["goal"], evaluation
    )

    related_scenarios = []
    if evaluation["overall_score"] < 60:
        related_scenarios = engine.generate_related_scenarios(
            scenario, count=2
        )

    return {
        "lesson_text": lesson_text,
        "key_principle": key_principle,
        "related_scenarios": related_scenarios
    }


def _extract_key_principle(goal: str, evaluation: dict) -> str:
    """
    Extract a key communication principle based on the goal.
    """
    principles = {
        "giving_feedback": (
            "💬 When giving feedback, use gentle words and focus on solutions "
            "instead of blaming."
        ),
        "polite_refusal": (
            "🤝 A polite refusal starts with thanks, explains the reason, "
            "and may offer an alternative."
        ),
        "apologizing": (
            "🙏 A sincere apology includes taking responsibility, "
            "showing understanding, and promising to improve."
        ),
        "asking_for_help": (
            "🆘 Asking for help politely means being kind, clear, and thankful."
        )
    }

    return principles.get(
        goal,
        "💡 Good communication comes from respect, listening, and gentle words."
    )
