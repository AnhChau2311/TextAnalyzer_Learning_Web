lexer grammar SentenceLexer;

// ===== Greeting and Thanking (Chào hỏi và cảm ơn) =====
GREETING
    : 'hello' | 'hi' | 'hey' | 'good morning' | 'good afternoon' 
    | 'good evening' | 'greetings'
    ;

THANK_YOU
    : 'thank you' | 'thanks' | 'thank' | 'appreciate'
    | 'grateful' | 'thankful'
    ;

// ===== Softening words (Từ làm mềm giọng) =====
SOFT_WORD
    : 'think' | 'maybe' | 'please' | 'try'
    | 'perhaps' | 'possibly' | 'kindly' | 'gently' | 'hopefully'
    | 'wondering' | 'consider' | 'suggest' | 'feel'
    | 'would you mind' | 'if you could' | 'when you get a chance'
    ;

// ===== Polite softeners and hedge words =====
HEDGE_WORD
    : 'kind of' | 'sort of' | 'a bit' | 'a little'
    | 'somewhat' | 'rather' | 'quite'
    ;

// ===== Strong / blaming / negative words =====
STRONG_WORD
    : 'wrong' | 'bad' | 'careless' | 'always' | 'stupid'
    | 'terrible' | 'awful' | 'horrible' | 'hate' | 'dumb'
    | 'idiot' | 'fool' | 'ugly' | 'worst' | 'useless'
    | 'annoying' | 'boring' | 'gross' | 'weird'
    ;

// ===== Command / demanding words =====
COMMAND_WORD
    : 'must' | 'have to' | 'need to' | 'should' | 'better'
    | 'immediately' | 'now' | 'right now'
    ;

// ===== Apology words =====
APOLOGY_WORD
    : 'sorry' | 'apologize' | 'apology' | 'forgive'
    | 'pardon' | 'excuse me' | 'my bad' | 'my fault'
    | 'regret' | 'oops'
    ;

// ===== Empathy words (Thể hiện đồng cảm) =====
EMPATHY_WORD
    : 'understand' | 'feel' | 'know' | 'realize'
    | 'see' | 'imagine' | 'empathize' | 'sympathize'
    ;

// ===== Polite modal verbs =====
POLITE_VERB
    : 'can' | 'may' | 'would' | 'could' | 'might'
    | 'shall' | 'will'
    ;

// ===== Request words (Yêu cầu) =====
REQUEST_WORD
    : 'help' | 'assist' | 'support' | 'need' | 'want'
    | 'like' | 'love' | 'prefer' | 'wish'
    ;

// ===== Positive adjectives =====
POSITIVE_ADJ
    : 'good' | 'great' | 'nice' | 'wonderful' | 'amazing'
    | 'beautiful' | 'lovely' | 'awesome' | 'fantastic'
    | 'excellent' | 'perfect' | 'sweet' | 'kind'
    | 'helpful' | 'friendly' | 'fun' | 'cool'
    ;

// ===== Negative emotions =====
NEGATIVE_EMOTION
    : 'sad' | 'angry' | 'upset' | 'mad' | 'frustrated'
    | 'disappointed' | 'hurt' | 'annoyed' | 'worried'
    ;

// ===== Positive emotions =====
POSITIVE_EMOTION
    : 'happy' | 'glad' | 'excited' | 'joyful' | 'pleased'
    | 'delighted' | 'thrilled' | 'cheerful'
    ;

// ===== Ownership and possession =====
POSSESSIVE
    : 'my' | 'your' | 'his' | 'her' | 'our' | 'their'
    | 'mine' | 'yours' | 'ours' | 'theirs'
    ;

// ===== Personal pronouns =====
PRONOUN
    : 'i' | 'you' | 'he' | 'she' | 'we' | 'they'
    | 'me' | 'him' | 'her' | 'us' | 'them'
    | 'it'
    ;

// ===== Question words =====
QUESTION_WORD
    : 'what' | 'when' | 'where' | 'who' | 'why' | 'how'
    | 'which' | 'whose'
    ;

// ===== Time references =====
TIME_WORD
    : 'today' | 'tomorrow' | 'yesterday' | 'now' | 'later'
    | 'soon' | 'before' | 'after' | 'always' |
    | 'sometimes' | 'often' | 'usually'
    ;

// ===== Conjunctions =====
CONJUNCTION
    : 'and' | 'but' | 'or' | 'so' | 'because' | 'if'
    | 'when' | 'while' | 'although' | 'however'
    | 'therefore' | 'moreover' | 'furthermore'
    ;

// ===== Negation =====
NEGATION
    : 'not' | 'no' | 'neither' | 'nor' | 'none'
    | 'nobody' | 'nothing' | 'nowhere' | 'never'
    | 'don\'t' | 'doesn\'t' | 'didn\'t' | 'won\'t'
    | 'wouldn\'t' | 'couldn\'t' | 'shouldn\'t'
    | 'can\'t' | 'cannot' | 'isn\'t' | 'aren\'t'
    ;

// ===== Articles =====
ARTICLE
    : 'a' | 'an' | 'the'
    ;

// ===== Prepositions =====
PREPOSITION
    : 'in' | 'on' | 'at' | 'to' | 'from' | 'with' | 'by'
    | 'for' | 'about' | 'of' | 'over' | 'under' | 'between'
    | 'through' | 'during' | 'before' | 'after' | 'above'
    | 'below' | 'near' | 'behind' | 'beside'
    ;

// ===== Numbers =====
NUMBER
    : [0-9]+ | 'one' | 'two' | 'three' | 'four' | 'five'
    | 'six' | 'seven' | 'eight' | 'nine' | 'ten'
    | 'first' | 'second' | 'third'
    ;

// ===== Common verbs =====
COMMON_VERB
    : 'is' | 'am' | 'are' | 'was' | 'were' | 'be' | 'been'
    | 'have' | 'has' | 'had' | 'do' | 'does' | 'did'
    | 'make' | 'made' | 'go' | 'went' | 'come' | 'came'
    | 'take' | 'took' | 'give' | 'gave' | 'get' | 'got'
    | 'see' | 'saw' | 'know' | 'knew' | 'thought'
    | 'say' | 'said' | 'tell' | 'told'
    ;

// ===== General words =====
WORD
    : [a-zA-Z]+
    | [a-zA-Z]+ '\'' [a-zA-Z]+  // contractions like "don't", "it's"
    ;

// ===== Punctuation =====
PUNCT
    : [.!?]
    ;

COMMA
    : ','
    ;

SEMICOLON
    : ';'
    ;

COLON
    : ':'
    ;

QUOTE
    : '"' | '\''
    ;

// ===== Emoticons and emojis (basic text versions) =====
EMOTICON
    : ':)' | ':(' | ':D' | ':P' | ';)' | '<3'
    | ':-)' | ':-(' | ':-D' | ':-P' | ';-)'
    ;

// ===== Whitespace =====
WS
    : [ \t\r\n]+ -> skip
    ;