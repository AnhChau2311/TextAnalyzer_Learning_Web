parser grammar SentenceParser;

options {
    tokenVocab = SentenceLexer;
}

// ===== Root rule =====
sentence
    : greeting? element+ closing? PUNCT?
    ;

// ===== Greeting pattern =====
greeting
    : GREETING COMMA?
    ;

// ===== Closing pattern =====
closing
    : THANK_YOU
    | polite_closing
    ;

polite_closing
    : SOFT_WORD PUNCT?
    | APOLOGY_WORD PUNCT?
    ;

// ===== Main element =====
element
    : polite_phrase
    | apology_phrase
    | request_phrase
    | emotional_expression
    | strong_expression
    | question_phrase
    | statement_phrase
    | softener
    | basic_word
    | punctuation_element
    ;

// ===== Polite phrase patterns =====
polite_phrase
    : SOFT_WORD
    | POLITE_VERB PRONOUN? SOFT_WORD?
    | HEDGE_WORD
    ;


// ===== Apology phrase patterns =====
apology_phrase
    : APOLOGY_WORD
    | PRONOUN COMMON_VERB APOLOGY_WORD
    | APOLOGY_WORD PREPOSITION? object_phrase?
    ;

// ===== Request phrase patterns =====
request_phrase
    : POLITE_VERB PRONOUN REQUEST_WORD
    | REQUEST_WORD help_pattern?
    | SOFT_WORD PRONOUN POLITE_VERB
    ;

help_pattern
    : PREPOSITION? PRONOUN?
    | PREPOSITION object_phrase
    ;

// ===== Statement phrase =====
statement_phrase
    : subject_phrase? verb_phrase object_phrase?
    | PRONOUN feeling_phrase
    ;

subject_phrase
    : PRONOUN
    | POSSESSIVE WORD
    | ARTICLE? WORD
    ;

verb_phrase
    : POLITE_VERB
    | COMMON_VERB
    ;

object_phrase
    : ARTICLE? POSSESSIVE? WORD+
    | PRONOUN
    ;

// ===== Feeling and emotion phrases =====
feeling_phrase
    : COMMON_VERB emotional_state
    | emotional_state
    ;

emotional_state
    : POSITIVE_EMOTION
    | NEGATIVE_EMOTION
    | POSITIVE_ADJ
    | STRONG_WORD
    ;

emotional_expression
    : EMPATHY_WORD
    | POSITIVE_EMOTION
    | NEGATIVE_EMOTION
    | EMOTICON
    ;

// ===== Question phrase =====
question_phrase
    : QUESTION_WORD
    | POLITE_VERB PRONOUN
    | QUESTION_WORD COMMON_VERB? PRONOUN?
    ;

// ===== Softener =====
softener
    : SOFT_WORD
    | HEDGE_WORD
    ;

// ===== Strong expression (negative) =====
strong_expression
    : STRONG_WORD
    | COMMAND_WORD
    | NEGATION POSITIVE_ADJ
    | NEGATION SOFT_WORD
    ;

// ===== Basic building blocks =====
basic_word
    : GREETING
    | POSSESSIVE
    | PRONOUN
    | ARTICLE
    | PREPOSITION
    | CONJUNCTION
    | NUMBER
    | TIME_WORD
    | WORD
    ;

punctuation_element
    : COMMA
    | SEMICOLON
    | COLON
    | QUOTE
    ;
