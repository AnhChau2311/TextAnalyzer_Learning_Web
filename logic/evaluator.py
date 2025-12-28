"""
evaluator.py - Combine analyzer-based scoring with grammar-driven model examples

AI is used ONLY to generate IDEAL MODEL SENTENCES.
Analyzer is the SINGLE SOURCE OF TRUTH for scoring.
Designed for children aged 6–10.
"""

from openai import OpenAI
from analysis.analyzer import analyze_sentence

client = OpenAI()


class ResponseEvaluator:
    """
    Evaluate responses using:
    - Analyzer as the only scoring authority
    - Rule-based, child-friendly feedback
    - Grammar- and context-driven MODEL examples (not rewrites)
    - Multi-layer validation for AI output
    """

    def __init__(self):
        self.client = client

        # =====================================================
        # GRAMMAR RUBRIC PER GOAL (AUTHORITATIVE)
        # =====================================================
        self.grammar_rubric = {
            "giving_feedback": {
                "required": [
                    "GREETING",
                    "POSITIVE_COMMENT",
                    "EMPATHY",
                    "GENTLE_SUGGESTION"
                ],
                "description":
                    "Say something nice, show understanding, and suggest improvement gently."
            },
            "expressing_disagreement": {
                "required": [
                    "ACKNOWLEDGEMENT",
                    "HEDGE",
                    "ALTERNATIVE_IDEA"
                ],
                "description":
                    "Respect the idea first, then share a different opinion politely."
            },
            "polite_refusal": {
                "required": [
                    "THANK_YOU",
                    "REASON",
                    "ALTERNATIVE_TIME"
                ],
                "description":
                    "Say thank you, explain kindly, and suggest another time."
            },
            "apologizing": {
                "required": [
                    "APOLOGY",
                    "RESPONSIBILITY",
                    "EMPATHY",
                    "PROMISE"
                ],
                "description":
                    "Say sorry clearly, show understanding, and promise to do better."
            },
            "asking_for_help": {
                "required": [
                    "GREETING",
                    "POLITE_REQUEST",
                    "CLARITY",
                    "THANK_YOU"
                ],
                "description":
                    "Ask politely, explain clearly, and say thank you."
            }
        }

        # =====================================================
        # SAFE FALLBACK MODEL SENTENCES (100% VERIFIED)
        # =====================================================
        self.fallback_examples = {
            "giving_feedback":
                "Hi Alex, I really like your work, and I understand accidents happen. Maybe next time we can be more careful together.",
            "expressing_disagreement":
                "I see your idea and think it is interesting, but maybe we could try another way that works better.",
            "polite_refusal":
                "Thank you for inviting me, but I feel very tired today, so maybe we can play together tomorrow.",
            "apologizing":
                "I am really sorry for what I said earlier, and I understand it hurt your feelings. I will be more careful next time.",
            "asking_for_help":
                "Hi, could you please help me with this problem? Thank you so much!"
        }

    # =====================================================
    # PUBLIC ENTRY POINT
    # =====================================================
    def evaluate_response(
        self,
        user_answer: str,
        scenario_goal: str,
        scenario_context: dict
    ) -> dict:
        """
        Full evaluation pipeline.
        """

        # ============================
        # STEP 1: Analyzer scores USER (single source of truth)
        # ============================
        analysis = analyze_sentence(user_answer, scenario_goal)

        # ============================
        # STEP 2: Child-friendly feedback (rule-based)
        # ============================
        feedback = self._generate_child_feedback(
            analysis, scenario_goal
        )

        # ============================
        # STEP 3: Generate MODEL example (if needed)
        # ============================
        model_example = None
        if analysis["overall_score"] < 70:
            model_example = self._generate_model_example(
                goal=scenario_goal,
                context=scenario_context
            )

        return {
            "user_answer": user_answer,
            "overall_score": analysis["overall_score"],
            "detailed_scores": analysis.get("scores", {}),
            "style": analysis.get("style"),
            "strengths": analysis.get("strengths", []),
            "weaknesses": analysis.get("weaknesses", []),
            "feedback": feedback,
            "improvement_example": model_example,
            "analysis": analysis
        }

    # =====================================================
    # CHILD-FRIENDLY FEEDBACK (NO AI)
    # =====================================================
    def _generate_child_feedback(self, analysis: dict, goal: str) -> dict:
        score = analysis["overall_score"]
        strengths = analysis.get("strengths", [])
        weaknesses = analysis.get("weaknesses", [])

        if score >= 85:
            praise = "🌟 Excellent! You spoke very kindly and clearly."
        elif score >= 70:
            praise = "😊 Nice job! You are speaking politely."
        elif score >= 55:
            praise = "💪 Good effort! You are learning."
        else:
            praise = "🌱 That’s okay. Everyone learns step by step."

        strength_message = ""
        if strengths:
            strength_message = "What you did well: " + ", ".join(strengths[:2])

        suggestion = ""
        if weaknesses:
            suggestion = "💡 You could add a little more understanding or a gentle suggestion."

        encouragement = {
            "giving_feedback":
                "🎯 Be kind and focus on helping, not blaming.",
            "expressing_disagreement":
                "🤝 Sharing ideas politely helps teamwork.",
            "polite_refusal":
                "🤍 Saying no kindly keeps friendships strong.",
            "apologizing":
                "🙏 A sincere apology helps fix mistakes.",
            "asking_for_help":
                "🆘 Polite asking makes people happy to help."
        }.get(goal, "⭐ Keep practicing!")

        return {
            "praise": praise,
            "strength_message": strength_message,
            "suggestion": suggestion,
            "encouragement": encouragement
        }

    # =====================================================
    # GRAMMAR + CONTEXT DRIVEN MODEL EXAMPLE (4-LAYER SAFE)
    # =====================================================
    def _generate_model_example(self, goal: str, context: dict) -> str:
        """
        Generate an IDEAL model sentence that:
        - Fits scenario context
        - Satisfies grammar rubric
        - Passes analyzer validation
        - Falls back safely if AI fails
        """

        rubric = self.grammar_rubric.get(goal)
        if not rubric:
            return self.fallback_examples.get(goal)

        prompt = f"""
You are a primary school teacher helping children aged 6–10
learn kind and polite communication.

SCENARIO TITLE:
{context['title']}

SCENARIO STORY:
{context['story']}

QUESTION:
{context['question']}

COMMUNICATION GOAL:
{goal}

GRAMMAR REQUIREMENTS:
{", ".join(rubric["required"])}

TASK:
Write ONE perfect example sentence that answers the question.

RULES:
- The sentence must fit the story exactly
- Use simple, friendly words
- Be kind, gentle, and encouraging
- Follow the grammar requirements
- ONE sentence only
- DO NOT copy or rewrite the child's answer
- DO NOT explain anything
- DO NOT use quotation marks
"""

        # ============================
        # AI ATTEMPTS (MAX 2 TRIES)
        # ============================
        for _ in range(2):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a kind primary school teacher."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.4,
                    max_tokens=80
                )

                sentence = response.choices[0].message.content.strip()

                if not sentence:
                    continue

                # ============================
                # STEP 4: Analyzer validates AI sentence
                # ============================
                ai_analysis = analyze_sentence(sentence, goal)

                if (
                    ai_analysis["overall_score"] >= 80
                    and ai_analysis["style"] in ("polite", "very_polite")
                ):
                    return sentence

            except Exception as e:
                print(f"AI error: {e}")

        # ============================
        # FINAL FALLBACK (GUARANTEED SAFE)
        # ============================
        return self.fallback_examples.get(goal)

# =====================================================
# COMPATIBILITY WRAPPER
# =====================================================
def evaluate_user_response(user_answer: str, scenario: dict) -> dict:
    evaluator = ResponseEvaluator()

    context = {
        "title": scenario["title"],
        "story": scenario["story"],
        "question": scenario["question"]
    }

    return evaluator.evaluate_response(
        user_answer=user_answer,
        scenario_goal=scenario["goal"],
        scenario_context=context
    )
