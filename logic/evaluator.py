"""
evaluator.py - Combine ANTLR-based analysis with grammar-driven model examples

AI is used ONLY to generate IDEAL MODEL SENTENCES.
It NEVER replaces scoring or analysis logic.
"""

from openai import OpenAI
from analysis.analyzer import analyze_sentence

client = OpenAI()


class ResponseEvaluator:
    """
    Evaluate responses from children aged 6–10 using:
    - Analyzer as the ONLY scoring authority
    - Rule-based child-friendly feedback
    - Grammar-driven MODEL examples (not user rewrites)
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
                    "EMPATHY_WORD",
                    "SOFT_WORD",
                    "SUGGESTION"
                ],
                "description":
                    "Be kind, show understanding, and suggest improvement gently."
            },
            "expressing_disagreement": {
                "required": [
                    "ACKNOWLEDGE",
                    "HEDGE_WORD",
                    "ALTERNATIVE"
                ],
                "description":
                    "Respect the idea first, then suggest another option politely."
            },
            "polite_refusal": {
                "required": [
                    "THANK_YOU",
                    "REASON",
                    "ALTERNATIVE"
                ],
                "description":
                    "Say thank you, explain softly, and suggest another time."
            },
            "apologizing": {
                "required": [
                    "APOLOGY_WORD",
                    "RESPONSIBILITY",
                    "EMPATHY_WORD",
                    "PROMISE"
                ],
                "description":
                    "Say sorry clearly, show understanding, and promise to improve."
            },
            "asking_for_help": {
                "required": [
                    "GREETING",
                    "POLITE_VERB",
                    "REQUEST",
                    "THANK_YOU"
                ],
                "description":
                    "Ask politely, clearly, and say thank you."
            }
        }

        # =====================================================
        # SAFE FALLBACK MODEL SENTENCES (100% GRAMMAR-CORRECT)
        # =====================================================
        self.fallback_examples = {
            "giving_feedback":
                "Hi Alex, I understand accidents happen, and maybe next time we can be more careful together.",
            "expressing_disagreement":
                "I see your idea, and I think it’s interesting, but maybe we could try another way that works better.",
            "polite_refusal":
                "Thank you for inviting me, but I feel very tired today, so maybe we can play together tomorrow.",
            "apologizing":
                "I’m really sorry for what I said earlier, and I understand it hurt your feelings. I will be more careful next time.",
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

        # STEP 1: Analyzer = single source of truth
        analysis = analyze_sentence(user_answer, scenario_goal)

        # STEP 2: Rule-based feedback for children
        feedback = self._generate_child_feedback(
            analysis, scenario_goal
        )

        # STEP 3: Grammar-driven MODEL example (only if score < 70)
        model_example = None
        if analysis["overall_score"] < 70:
            model_example = self._generate_model_example(
                goal=scenario_goal,
                context=scenario_context
            )

        return {
            "user_answer": user_answer,
            "overall_score": analysis["overall_score"],
            "detailed_scores": analysis["scores"],
            "style": analysis["style"],
            "strengths": analysis["strengths"],
            "weaknesses": analysis["weaknesses"],
            "feedback": feedback,
            "improvement_example": model_example,
            "antlr_analysis": analysis
        }

    # =====================================================
    # CHILD-FRIENDLY FEEDBACK (NO AI)
    # =====================================================
    def _generate_child_feedback(self, analysis: dict, goal: str) -> dict:
        score = analysis["overall_score"]
        strengths = analysis["strengths"]
        weaknesses = analysis["weaknesses"]

        if score >= 80:
            praise = "🌟 Excellent! Your sentence is very polite and thoughtful."
        elif score >= 60:
            praise = "😊 Nice job! You are speaking politely."
        elif score >= 40:
            praise = "💪 Good effort! Let’s try to make it even better."
        else:
            praise = "🌱 That’s okay. Learning takes practice!"

        strength_message = ""
        if strengths:
            strength_message = "What you did well: " + ", ".join(strengths[:2])

        suggestion = ""
        if weaknesses:
            suggestion = "💡 Try using gentle words and follow the polite speaking steps."

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
    # GRAMMAR-DRIVEN MODEL EXAMPLE (CORE FIX)
    # =====================================================
    def _generate_model_example(self, goal: str, context: dict) -> str:
        """
        Generate an IDEAL model sentence that:
        - Does NOT reuse user input
        - Satisfies grammar rubric
        - Scores high if analyzed
        """

        rubric = self.grammar_rubric.get(goal)
        if not rubric:
            return self.fallback_examples.get(goal)

        prompt = f"""
You are a primary school teacher.

SITUATION:
{context['title']}

GOAL:
{goal}

GRAMMAR REQUIREMENTS:
{", ".join(rubric["required"])}

INSTRUCTIONS:
- Write ONE perfect example sentence
- Follow the grammar requirements exactly
- Use simple words for children aged 6–10
- Be polite, kind, and natural
- DO NOT copy or rewrite the child's sentence
- DO NOT explain anything
- ONE sentence only

EXAMPLE OUTPUT STYLE:
Hi Alex, I understand accidents happen, and maybe next time we can be more careful together.

NOW WRITE THE SENTENCE:
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a kind primary school teacher."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=60
            )

            sentence = response.choices[0].message.content.strip()

            # SAFETY CHECK: never echo user input
            if sentence:
                return sentence

        except Exception as e:
            print(f"AI error: {e}")

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
