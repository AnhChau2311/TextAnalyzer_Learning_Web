from analysis.parser_runner import parse_sentence


def analyze_sentence(text: str) -> dict:
    """
    Analyze a sentence using lexical and semantic features
    to evaluate children's communication style.
    """
    tokens = parse_sentence(text)

    # Count occurrences of each token type
    token_counts = {}
    for token in tokens:
        token_counts[token] = token_counts.get(token, 0) + 1

    # Extract linguistic features
    analysis = {
        # Politeness-related features
        "has_greeting": "GREETING" in tokens,
        "has_thank_you": "THANK_YOU" in tokens,
        "has_softening": "SOFT_WORD" in tokens or "HEDGE_WORD" in tokens,
        "has_polite_verb": "POLITE_VERB" in tokens,
        "has_please": "please" in text.lower(),

        # Apology and empathy features
        "has_apology": "APOLOGY_WORD" in tokens,
        "has_empathy": "EMPATHY_WORD" in tokens,

        # Negative language features
        "has_strong": "STRONG_WORD" in tokens,
        "has_command": "COMMAND_WORD" in tokens,
        "has_negation": "NEGATION" in tokens,
        "has_negative_emotion": "NEGATIVE_EMOTION" in tokens,

        # Positive language features
        "has_positive_adj": "POSITIVE_ADJ" in tokens,
        "has_positive_emotion": "POSITIVE_EMOTION" in tokens,

        # Question-related features
        "has_question": "QUESTION_WORD" in tokens,

        # Quantitative counts
        "strong_word_count": token_counts.get("STRONG_WORD", 0),
        "soft_word_count": (
            token_counts.get("SOFT_WORD", 0) +
            token_counts.get("HEDGE_WORD", 0)
        ),
        "polite_element_count": (
            token_counts.get("SOFT_WORD", 0) +
            token_counts.get("HEDGE_WORD", 0) +
            token_counts.get("POLITE_VERB", 0) +
            token_counts.get("THANK_YOU", 0) +
            token_counts.get("GREETING", 0)
        ),

        # Debugging information
        "tokens": tokens,
        "token_counts": token_counts
    }

    # Compute politeness score
    analysis["politeness_score"] = calculate_politeness_score(analysis)

    # Determine overall communication style
    analysis["style"] = determine_style(analysis)

    # Infer communication goal
    analysis["goal"] = determine_goal(analysis, text)

    # Generate improvement suggestions
    analysis["suggestions"] = get_suggestions(analysis)

    return analysis


def calculate_politeness_score(analysis: dict) -> int:
    """
    Calculate a politeness score ranging from 0 to 100.
    """
    score = 50  # Base score

    # Increase score for polite elements
    if analysis["has_greeting"]:
        score += 10
    if analysis["has_thank_you"]:
        score += 10
    if analysis["has_softening"]:
        score += 15
    if analysis["has_polite_verb"]:
        score += 10
    if analysis["has_please"]:
        score += 10
    if analysis["has_apology"]:
        score += 10
    if analysis["has_empathy"]:
        score += 10
    if analysis["has_positive_adj"] or analysis["has_positive_emotion"]:
        score += 5

    # Decrease score for negative elements
    if analysis["has_strong"]:
        score -= 20 * analysis["strong_word_count"]
    if analysis["has_command"]:
        score -= 15
    if analysis["has_negative_emotion"]:
        score -= 10

    return max(0, min(100, score))


def determine_style(analysis: dict) -> str:
    """
    Determine the overall communication style.
    Possible values: gentle, harsh, mixed, polite, direct, neutral.
    """
    polite_count = analysis["polite_element_count"]
    strong_count = analysis["strong_word_count"]

    if polite_count >= 2 and strong_count == 0:
        return "gentle"
    elif strong_count >= 2 and polite_count == 0:
        return "harsh"
    elif strong_count > 0 and polite_count > 0:
        return "mixed"
    elif polite_count > 0:
        return "polite"
    elif strong_count > 0:
        return "direct"
    else:
        return "neutral"


def determine_goal(analysis: dict, text: str) -> str:
    """
    Infer the communicative intent of the sentence.
    """
    text_lower = text.lower()

    if analysis["has_apology"] or "sorry" in text_lower or "apologize" in text_lower:
        return "apologizing"

    if "help" in text_lower or "assist" in text_lower or "need" in text_lower:
        if analysis["has_polite_verb"] or analysis["has_softening"]:
            return "asking_for_help"
        return "demanding_help"

    if any(word in text_lower for word in ["no", "can't", "cannot", "won't", "unable"]):
        if analysis["has_softening"] or analysis["has_apology"]:
            return "polite_refusal"
        return "direct_refusal"

    if any(word in text_lower for word in ["think", "feel", "believe", "suggest"]):
        if analysis["has_strong"]:
            return "critical_feedback"
        if analysis["has_softening"]:
            return "gentle_feedback"
        return "giving_feedback"

    if analysis["has_thank_you"]:
        return "expressing_gratitude"

    if analysis["has_greeting"]:
        return "greeting"

    if analysis["has_question"] or text.strip().endswith("?"):
        return "asking_question"

    return "general_statement"


def get_suggestions(analysis: dict) -> list:
    """
    Generate improvement suggestions based on missing or weak features.
    """
    suggestions = []

    if not analysis["has_greeting"] and analysis["politeness_score"] < 70:
        suggestions.append("Try starting with a greeting such as 'Hi' or 'Hello'.")

    if analysis["has_strong"] and not analysis["has_softening"]:
        suggestions.append(
            "Try adding softening words like 'maybe', 'I think', or 'could'."
        )

    if analysis["has_command"] and not analysis["has_polite_verb"]:
        suggestions.append(
            "Consider using polite forms like 'could you' or 'would you'."
        )

    if analysis["goal"] in ["asking_for_help", "general_statement"] and not analysis["has_thank_you"]:
        suggestions.append("Try ending your sentence with 'thank you' or 'thanks'.")

    if analysis["has_apology"] and not analysis["has_empathy"]:
        suggestions.append(
            "Show empathy by saying phrases like 'I understand' or 'I realize'."
        )

    if analysis["strong_word_count"] >= 2:
        suggestions.append(
            "There are too many strong words. Try reducing them to sound gentler."
        )

    if analysis["politeness_score"] < 30:
        suggestions.append(
            "This sentence needs more politeness. Try adding 'please', 'thank you', or 'sorry'."
        )

    return suggestions


def get_detailed_feedback(analysis: dict, context: str = "general") -> dict:
    """
    Generate detailed feedback including strengths and areas for improvement.
    """
    score = analysis["politeness_score"]
    style = analysis["style"]

    feedback = {
        "score": score,
        "style": style,
        "summary": "",
        "strengths": [],
        "improvements": [],
        "example": ""
    }

    if score >= 80:
        feedback["summary"] = "Excellent! Your sentence is very polite and thoughtful."
    elif score >= 60:
        feedback["summary"] = "Good job! Your sentence is fairly polite."
    elif score >= 40:
        feedback["summary"] = "Not bad, but it could be improved to sound more polite."
    else:
        feedback["summary"] = "This sentence needs improvement to sound kinder and more respectful."

    if analysis["has_greeting"]:
        feedback["strengths"].append("Uses a greeting")
    if analysis["has_thank_you"]:
        feedback["strengths"].append("Includes a thank-you expression")
    if analysis["has_softening"]:
        feedback["strengths"].append("Uses softening language")
    if analysis["has_apology"]:
        feedback["strengths"].append("Includes an apology")
    if analysis["has_empathy"]:
        feedback["strengths"].append("Shows empathy")

    feedback["improvements"] = analysis["suggestions"]

    return feedback
