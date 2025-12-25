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
    - Goal appropriateness (soft)
    - Child-friendly communication
    """

    def __init__(self):
        # ============================
        # SENTIMENT PATTERNS
        # ============================
        self.sentiment_patterns = {
            "positive": [
                r"\b(okay|ok|fine|good|nice|great|happy|glad)\b"
            ],
            "negative": [
                r"\b(hate|angry|sad|upset|terrible|awful|bad)\b",
                r"\b(stupid|dumb|worst)\b"
            ],
            "empathy": [
                r"\b(understand|know|feel|realize)\b",
                r"\b(didn't mean|accident)\b"
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
            r"\b(you must|give me|do it now)\b"
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
            "strengths": self._strengths(text_lower, sentiment),
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
    # SCORING (NEW RUBRIC)
    # =====================================================
    def _calculate_scores(self, text, sentiment, structure, goal):
        score = 0

        # 1️⃣ Emotional safety (40)
        if sentiment["negative"] == 0:
            score += 15
        if sentiment["empathy"] > 0:
            score += 15
        if sentiment["positive"] > 0 or sentiment["empathy"] > 0:
            score += 10

        # 2️⃣ Politeness basics (25)
        score += min(25, structure["polite"] * 5)

        # 3️⃣ Goal appropriateness (20 - soft)
        if goal == "giving_feedback":
            if sentiment["empathy"] > 0 or "maybe" in text:
                score += 20
        elif goal == "polite_refusal":
            if "thank" in text or "because" in text:
                score += 20
        elif goal == "apologizing":
            if sentiment["apology"] > 0:
                score += 20
        elif goal == "asking_for_help":
            if re.search(r"\b(could|can|please)\b", text):
                score += 20
        else:
            score += 15

        # 4️⃣ Structure clarity (15)
        score += 10
        if structure["command"] == 0:
            score += 5

        # Penalties
        if sentiment["negative"] > 0:
            score -= 10
        if structure["command"] > 0:
            score -= 10

        return {
            "overall": max(0, min(100, int(score)))
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

    def _strengths(self, text, sentiment):
        s = []
        if sentiment["empathy"] > 0:
            s.append("Shows understanding and kindness")
        if "hello" in text or "hi" in text:
            s.append("Uses a friendly greeting")
        return s

    def _weaknesses(self, text, sentiment, goal):
        w = []
        if sentiment["empathy"] == 0:
            w.append("Could show a little more understanding")
        if goal == "giving_feedback" and "maybe" not in text:
            w.append("Could add a gentle suggestion")
        return w


# =====================================================
# COMPATIBILITY WRAPPER
# =====================================================
def analyze_sentence(text: str, scenario_goal: str = None) -> dict:
    analyzer = ContextAwareAnalyzer()
    return analyzer.analyze_sentence(text, scenario_goal)
