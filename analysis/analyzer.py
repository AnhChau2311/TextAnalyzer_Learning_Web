"""
analyzer.py - Context-aware sentence analyzer (Education-first version)

Designed for children aged 6–10.
Prioritizes emotional safety, kindness, and clarity over technical perfection.
"""

import re
from analysis.parser_runner import parse_sentence, get_token_details


class ContextAwareAnalyzer:
    """
    Analyze a sentence with emphasis on:
    - Emotional safety
    - Politeness basics
    - Goal appropriateness (soft, flexible)
    - Child-friendly communication
    """

    def __init__(self):
        # ============================
        # SENTIMENT PATTERNS
        # ============================
        self.sentiment_patterns = {
            "positive": [
                r"\b(okay|ok|fine|good|nice|great|happy|glad|like|love)\b"
            ],
            "negative": [
                r"\b(hate|angry|sad|upset|terrible|awful|bad)\b",
                r"\b(stupid|dumb|worst)\b"
            ],
            "empathy": [
                r"\b(understand|know|feel|realize)\b",
                r"\b(accident|didn't mean|it's okay|it is okay)\b"
            ],
            "apology": [
                r"\b(sorry|apologize|my fault|my bad)\b"
            ]
        }

        # ============================
        # STRUCTURE PATTERNS
        # ============================
        self.polite_patterns = [
            r"\b(hi|hello)\b",
            r"\b(please)\b",
            r"\b(thank you|thanks)\b",
            r"\b(could you|would you|can i|may i)\b",
            r"\b(maybe|i think|perhaps)\b"
        ]

        self.command_patterns = [
            r"\b(you must|do it now|give me|stop that)\b"
        ]

    # =====================================================
    # PUBLIC ENTRY
    # =====================================================
    def analyze_sentence(self, text: str, scenario_goal: str = None) -> dict:
        text_lower = text.lower()

        tokens = parse_sentence(text)
        token_details = get_token_details(text)

        sentiment = self._analyze_sentiment(text_lower)
        structure = self._analyze_structure(text_lower)

        scores = self._calculate_scores(
            text_lower,
            sentiment,
            structure,
            scenario_goal
        )

        style = self._determine_style(scores)

        return {
            "tokens": tokens,
            "token_details": token_details,
            "sentiment": sentiment,
            "structure": structure,
            "scores": scores,
            "overall_score": scores["overall"],
            "style": style,
            "strengths": self._strengths(text_lower, sentiment, structure),
            "weaknesses": self._weaknesses(text_lower, sentiment, scenario_goal)
        }

    # =====================================================
    # ANALYSIS HELPERS
    # =====================================================
    def _analyze_sentiment(self, text: str) -> dict:
        result = {}
        for k, patterns in self.sentiment_patterns.items():
            result[k] = sum(len(re.findall(p, text)) for p in patterns)
        return result

    def _analyze_structure(self, text: str) -> dict:
        polite = sum(len(re.findall(p, text)) for p in self.polite_patterns)
        command = sum(len(re.findall(p, text)) for p in self.command_patterns)
        return {
            "polite": polite,
            "command": command
        }

    # =====================================================
    # SCORING (EDUCATION-FIRST RUBRIC + BREAKDOWN)
    # =====================================================
    def _calculate_scores(self, text, sentiment, structure, goal):
        total = 0
        breakdown = {}

        # =================================================
        # 1️⃣ Emotional Safety (max 40)
        # =================================================
        emo_score = 0
        emo_reasons = []

        if sentiment["negative"] == 0:
            emo_score += 15
            emo_reasons.append("+15: Uses no hurtful or angry words")

        if sentiment["empathy"] > 0:
            emo_score += 15
            emo_reasons.append("+15: Shows understanding or kindness")

        if sentiment["positive"] > 0:
            emo_score += 10
            emo_reasons.append("+10: Says something positive")

        breakdown["emotional_safety"] = {
            "score": emo_score,
            "max": 40,
            "reasons": emo_reasons
        }
        total += emo_score

        # =================================================
        # 2️⃣ Politeness Basics (max 25)
        # =================================================
        polite_score = min(25, structure["polite"] * 5)
        polite_reasons = []

        if structure["polite"] > 0:
            polite_reasons.append(
                f"+{polite_score}: Uses polite or gentle words"
            )

        breakdown["politeness"] = {
            "score": polite_score,
            "max": 25,
            "reasons": polite_reasons
        }
        total += polite_score

        # =================================================
        # 3️⃣ Goal Appropriateness (max 20)
        # =================================================
        goal_score = 0
        goal_reasons = []

        if goal == "giving_feedback":
            if sentiment["positive"] > 0:
                goal_score += 10
                goal_reasons.append(
                    "+10: Says something nice before giving feedback"
                )
            if "maybe" in text or sentiment["empathy"] > 0:
                goal_score += 10
                goal_reasons.append(
                    "+10: Gives a gentle suggestion"
                )

        elif goal == "polite_refusal":
            if "thank" in text:
                goal_score += 10
                goal_reasons.append("+10: Says thank you politely")
            if "because" in text or "but" in text:
                goal_score += 10
                goal_reasons.append(
                    "+10: Explains reason kindly"
                )

        elif goal == "apologizing":
            if sentiment["apology"] > 0:
                goal_score += 20
                goal_reasons.append("+20: Gives a clear apology")
            elif sentiment["empathy"] > 0:
                goal_score += 10
                goal_reasons.append("+10: Shows understanding")

        elif goal == "asking_for_help":
            if re.search(r"\b(could|can|please)\b", text):
                goal_score += 20
                goal_reasons.append(
                    "+20: Asks for help politely"
                )

        else:
            goal_score += 15
            goal_reasons.append("+15: Communicates kindly")

        breakdown["goal_fit"] = {
            "score": goal_score,
            "max": 20,
            "reasons": goal_reasons
        }
        total += goal_score

        # =================================================
        # 4️⃣ Clarity & Tone (max 15)
        # =================================================
        clarity_score = 10
        clarity_reasons = ["+10: Sentence is clear and easy to understand"]

        if structure["command"] == 0:
            clarity_score += 5
            clarity_reasons.append(
                "+5: Does not sound bossy or commanding"
            )

        breakdown["clarity"] = {
            "score": clarity_score,
            "max": 15,
            "reasons": clarity_reasons
        }
        total += clarity_score

        # Gentle internal penalties (NOT shown to kids)
        if sentiment["negative"] > 0:
            total -= 5
        if structure["command"] > 0:
            total -= 5

        return {
            "overall": max(0, min(100, int(total))),
            "breakdown": breakdown
        }

    # =====================================================
    # STYLE & FEEDBACK
    # =====================================================
    def _determine_style(self, scores):
        s = scores["overall"]
        if s >= 85:
            return "very_polite"
        if s >= 70:
            return "polite"
        if s >= 55:
            return "neutral"
        if s >= 40:
            return "needs_improvement"
        return "harsh"

    def _strengths(self, text, sentiment, structure):
        s = []
        if sentiment["empathy"] > 0:
            s.append("Shows understanding and kindness")
        if sentiment["positive"] > 0:
            s.append("Says something positive first")
        if structure["polite"] > 0:
            s.append("Uses polite or gentle words")
        return s

    def _weaknesses(self, text, sentiment, goal):
        w = []
        if sentiment["empathy"] == 0:
            w.append("Could show a little more understanding")
        if goal == "giving_feedback" and "maybe" not in text:
            w.append("Could add a gentle suggestion")
        if goal == "asking_for_help" and "please" not in text:
            w.append("Could sound a bit more polite")
        return w


# =====================================================
# COMPATIBILITY WRAPPER
# =====================================================
def analyze_sentence(text: str, scenario_goal: str = None) -> dict:
    analyzer = ContextAwareAnalyzer()
    return analyzer.analyze_sentence(text, scenario_goal)
