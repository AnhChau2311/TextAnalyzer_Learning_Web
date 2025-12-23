from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from analysis.generated.SentenceLexer import SentenceLexer
from analysis.generated.SentenceParser import SentenceParser


class SentenceErrorListener(ErrorListener):
    """
    Custom error listener to capture lexical and syntax errors
    during parsing.
    """
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            "line": line,
            "column": column,
            "message": msg,
            "symbol": str(offendingSymbol)
        })


def parse_sentence(text: str, return_errors: bool = False):
    """
    Run ANTLR lexer and parser on the input text.

    Args:
        text: Input sentence to be analyzed
        return_errors: If True, return a tuple (tokens, errors)

    Returns:
        A list of token type names,
        or (tokens, errors) if return_errors is True
    """
    text = text.strip()
    if not text:
        return [] if not return_errors else ([], [])

    input_stream = InputStream(text.lower())
    lexer = SentenceLexer(input_stream)

    error_listener = SentenceErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    tokens = []
    for token in token_stream.tokens:
        if token.type != -1:  # Skip EOF
            token_name = lexer.symbolicNames[token.type]
            if token_name:
                tokens.append(token_name)

    parser = SentenceParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        parser.sentence()
    except Exception as e:
        error_listener.errors.append({
            "line": 0,
            "column": 0,
            "message": str(e),
            "symbol": "N/A"
        })

    if return_errors:
        return tokens, error_listener.errors

    return tokens


def get_token_details(text: str) -> list:
    """
    Retrieve detailed information for each token,
    including its type, text, and position.
    """
    input_stream = InputStream(text.lower())
    lexer = SentenceLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    token_details = []
    for token in token_stream.tokens:
        if token.type != -1:  # Skip EOF
            token_name = lexer.symbolicNames[token.type]
            if token_name:
                token_details.append({
                    "type": token_name,
                    "text": token.text,
                    "start": token.start,
                    "stop": token.stop,
                    "line": token.line,
                    "column": token.column
                })

    return token_details


def analyze_sentence_structure(text: str) -> dict:
    """
    Perform a detailed structural analysis of the sentence.

    Returns:
        A dictionary containing structural and syntactic information.
    """
    tokens, errors = parse_sentence(text, return_errors=True)
    token_details = get_token_details(text)

    structure = {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "token_count": len(tokens),
        "unique_token_types": len(set(tokens)),
        "tokens": tokens,
        "token_details": token_details,
        "has_punctuation": any(
            t in ["PUNCT", "COMMA", "SEMICOLON", "COLON"] for t in tokens
        ),
        "is_question": "QUESTION_WORD" in tokens or text.strip().endswith("?"),
        "is_exclamation": text.strip().endswith("!"),
        "word_count": len([t for t in tokens if t == "WORD"])
    }

    return structure


def get_token_categories(tokens: list) -> dict:
    """
    Categorize tokens into linguistic groups.

    Returns:
        A dictionary mapping category names to token lists.
    """
    categories = {
        "politeness": [],
        "emotions": [],
        "grammar": [],
        "content": [],
        "negation": [],
        "questions": []
    }

    politeness_tokens = [
        "GREETING", "THANK_YOU", "SOFT_WORD", "HEDGE_WORD",
        "POLITE_VERB", "APOLOGY_WORD", "EMPATHY_WORD"
    ]

    emotion_tokens = [
        "POSITIVE_EMOTION", "NEGATIVE_EMOTION",
        "POSITIVE_ADJ", "STRONG_WORD", "EMOTICON"
    ]

    grammar_tokens = [
        "PRONOUN", "ARTICLE", "PREPOSITION",
        "CONJUNCTION", "COMMON_VERB", "POSSESSIVE"
    ]

    negation_tokens = ["NEGATION", "COMMAND_WORD"]
    question_tokens = ["QUESTION_WORD"]

    for token in tokens:
        if token in politeness_tokens:
            categories["politeness"].append(token)
        if token in emotion_tokens:
            categories["emotions"].append(token)
        if token in grammar_tokens:
            categories["grammar"].append(token)
        if token in negation_tokens:
            categories["negation"].append(token)
        if token in question_tokens:
            categories["questions"].append(token)
        if token == "WORD":
            categories["content"].append(token)

    return categories
