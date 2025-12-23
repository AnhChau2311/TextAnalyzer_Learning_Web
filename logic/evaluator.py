"""
evaluator.py - Evaluate children's responses using ANTLR + OpenAI
"""

import os
import json
from openai import OpenAI

from analysis.analyzer import analyze_sentence
from analysis.parser_runner import get_token_details


client = OpenAI()

class ResponseEvaluator:
    """
    Evaluate and analyze a child's response in a flexible,
    educational, and encouraging way.
    """

    def __init__(self):
        self.client = client

    def evaluate_response(
        self,
        user_answer: str,
        scenario_goal: str,
        scenario_context: dict
    ) -> dict:
        """
        Perform a full evaluation of the child's answer.

        Args:
            user_answer: The child's answer
            scenario_goal: Communication goal (giving_feedback, polite_refusal, etc.)
            scenario_context: {title, story, question}

        Returns:
            A dictionary containing detailed evaluation results
        """
        antlr_analysis = analyze_sentence(user_answer)
        token_details = get_token_details(user_answer)

        ai_evaluation = self._get_ai_evaluation(
            answer=user_answer,
            goal=scenario_goal,
            context=scenario_context,
            antlr_data=antlr_analysis
        )

        highlighted_words = self._highlight_words(
            user_answer,
            token_details,
            antlr_analysis
        )

        return {
            "user_answer": user_answer,
            "antlr_analysis": antlr_analysis,
            "ai_evaluation": ai_evaluation,
            "highlighted_words": highlighted_words,
            "overall_score": self._calculate_overall_score(
                antlr_analysis,
                ai_evaluation
            ),
        }

    def _get_ai_evaluation(
        self,
        answer: str,
        goal: str,
        context: dict,
        antlr_data: dict
    ) -> dict:
        """
        Use OpenAI to generate a flexible, child-friendly evaluation.
        """
        goal_descriptions = {
            "giving_feedback": "give feedback in a kind and constructive way",
            "polite_refusal": "refuse politely without hurting others",
            "apologizing": "apologize sincerely and responsibly",
            "asking_for_help": "ask for help politely and clearly",
        }

        goal_description = goal_descriptions.get(goal, "communicate effectively")

        prompt = f"""
You are an experienced primary school teacher helping children
learn communication skills.

SITUATION TITLE: {context['title']}
STORY: {context['story']}
QUESTION: {context['question']}
GOAL: Learn how to {goal_description}

CHILD'S ANSWER:
"{answer}"

TECHNICAL ANALYSIS:
- Politeness score: {antlr_data['politeness_score']}/100
- Style: {antlr_data['style']}
- Has greeting: {antlr_data['has_greeting']}
- Has thank you: {antlr_data['has_thank_you']}
- Has apology: {antlr_data['has_apology']}
- Uses strong words: {antlr_data['has_strong']}

Evaluate the response and return JSON ONLY in the following format:

{{
    "is_appropriate": true/false,
    "tone": "gentle | harsh | neutral | mixed",
    "feedback_summary": "1–2 friendly and encouraging sentences",
    "strengths": ["strength 1", "strength 2"],
    "areas_for_improvement": ["improvement 1", "improvement 2"],
    "creativity_score": 0-10,
    "empathy_score": 0-10
}}

Guidelines:
- Do not be harsh; the child is learning
- Always find something positive to praise
- Suggestions should be simple and easy to understand
- Use friendly and supportive language
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a friendly, experienced teacher who encourages "
                            "children to learn communication skills."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            return json.loads(response.choices[0].message.content)

        except Exception as e:
            print(f"OpenAI error: {e}")
            return {
                "is_appropriate": True,
                "tone": "neutral",
                "feedback_summary": "Thank you for sharing your answer!",
                "strengths": ["You made an effort"],
                "areas_for_improvement": ["Try adding a greeting or saying thank you"],
                "creativity_score": 5,
                "empathy_score": 5
            }

    def _highlight_words(
        self,
        text: str,
        token_details: list,
        analysis: dict
    ) -> list:
        """
        Highlight important words with colors and tooltips.

        Returns:
            [
                {
                    "word": "hello",
                    "color": "success",
                    "tooltip": "Polite greeting!",
                    "start": int,
                    "stop": int
                }
            ]
        """
        highlighted = []

        color_map = {
            "GREETING": {"color": "success", "tooltip": "Polite greeting 👋"},
            "THANK_YOU": {"color": "success", "tooltip": "Good manners 🙏"},
            "SOFT_WORD": {"color": "success", "tooltip": "Softening word ✨"},
            "POLITE_VERB": {"color": "success", "tooltip": "Polite verb 💚"},
            "APOLOGY_WORD": {"color": "success", "tooltip": "Sincere apology 🙇"},
            "EMPATHY_WORD": {"color": "success", "tooltip": "Shows empathy 💙"},
            "POSITIVE_ADJ": {"color": "success", "tooltip": "Positive word ⭐"},
            "POSITIVE_EMOTION": {"color": "success", "tooltip": "Positive emotion 😊"},
            "HEDGE_WORD": {"color": "info", "tooltip": "Gentle softener 🌟"},
            "STRONG_WORD": {"color": "danger", "tooltip": "Strong word ⚠️"},
            "COMMAND_WORD": {"color": "warning", "tooltip": "Commanding tone ⚡"},
            "NEGATIVE_EMOTION": {"color": "warning", "tooltip": "Negative emotion 😔"},
        }

        for token in token_details:
            token_type = token["type"]
            if token_type in color_map:
                info = color_map[token_type]
                highlighted.append({
                    "word": token["text"],
                    "color": info["color"],
                    "tooltip": info["tooltip"],
                    "start": token["start"],
                    "stop": token["stop"]
                })

        return highlighted

    def _calculate_overall_score(
        self,
        antlr_analysis: dict,
        ai_evaluation: dict
    ) -> int:
        """
        Calculate the final score by combining ANTLR and AI scores.
        """
        antlr_score = antlr_analysis["politeness_score"]
        creativity = ai_evaluation.get("creativity_score", 5) * 10
        empathy = ai_evaluation.get("empathy_score", 5) * 10

        overall = (
            antlr_score * 0.5 +
            creativity * 0.25 +
            empathy * 0.25
        )

        return int(overall)


def evaluate_user_response(user_answer: str, scenario: dict) -> dict:
    """
    Helper function for evaluating a child's answer.

    Args:
        user_answer: The child's answer
        scenario: {id, title, story, question, goal}

    Returns:
        Evaluation result dictionary
    """
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
