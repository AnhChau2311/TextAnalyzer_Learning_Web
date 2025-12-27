# Generated from /Users/anhchau/Documents/Principles of Programming Languages/TextAnalyzer_Learning_Web/analysis/grammar/SentenceParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,3,0,44,8,0,1,0,4,0,47,8,0,11,0,12,0,48,1,0,3,0,52,8,0,1,
        0,3,0,55,8,0,1,1,1,1,3,1,59,8,1,1,2,1,2,3,2,63,8,2,1,3,1,3,3,3,67,
        8,3,1,3,1,3,3,3,71,8,3,3,3,73,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,85,8,4,1,5,1,5,1,5,3,5,90,8,5,1,5,3,5,93,8,5,1,5,1,
        5,3,5,97,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,105,8,6,1,6,3,6,108,8,6,
        3,6,110,8,6,1,7,1,7,1,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,7,3,7,122,
        8,7,1,8,3,8,125,8,8,1,8,3,8,128,8,8,1,8,1,8,3,8,132,8,8,1,9,3,9,
        135,8,9,1,9,1,9,3,9,139,8,9,1,9,1,9,3,9,143,8,9,1,10,1,10,1,10,1,
        10,3,10,149,8,10,1,10,3,10,152,8,10,1,11,1,11,1,12,3,12,157,8,12,
        1,12,3,12,160,8,12,1,12,4,12,163,8,12,11,12,12,12,164,1,12,3,12,
        168,8,12,1,13,1,13,1,13,3,13,173,8,13,1,14,1,14,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,3,16,184,8,16,1,16,3,16,187,8,16,3,16,189,8,16,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,199,8,18,1,19,1,19,
        1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,0,6,2,0,9,9,23,24,2,0,5,5,11,13,3,0,8,8,12,13,30,
        30,1,0,3,4,4,0,1,1,14,15,17,18,20,24,1,0,26,29,234,0,43,1,0,0,0,
        2,56,1,0,0,0,4,62,1,0,0,0,6,72,1,0,0,0,8,84,1,0,0,0,10,96,1,0,0,
        0,12,109,1,0,0,0,14,121,1,0,0,0,16,131,1,0,0,0,18,142,1,0,0,0,20,
        151,1,0,0,0,22,153,1,0,0,0,24,167,1,0,0,0,26,172,1,0,0,0,28,174,
        1,0,0,0,30,176,1,0,0,0,32,188,1,0,0,0,34,190,1,0,0,0,36,198,1,0,
        0,0,38,200,1,0,0,0,40,202,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,43,
        44,1,0,0,0,44,46,1,0,0,0,45,47,3,8,4,0,46,45,1,0,0,0,47,48,1,0,0,
        0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,52,3,4,2,0,51,50,
        1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,55,5,25,0,0,54,53,1,0,0,0,
        54,55,1,0,0,0,55,1,1,0,0,0,56,58,5,1,0,0,57,59,5,26,0,0,58,57,1,
        0,0,0,58,59,1,0,0,0,59,3,1,0,0,0,60,63,5,2,0,0,61,63,3,6,3,0,62,
        60,1,0,0,0,62,61,1,0,0,0,63,5,1,0,0,0,64,66,5,3,0,0,65,67,5,25,0,
        0,66,65,1,0,0,0,66,67,1,0,0,0,67,73,1,0,0,0,68,70,5,7,0,0,69,71,
        5,25,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,64,1,0,0,0,
        72,68,1,0,0,0,73,7,1,0,0,0,74,85,3,10,5,0,75,85,3,12,6,0,76,85,3,
        14,7,0,77,85,3,18,9,0,78,85,3,32,16,0,79,85,3,30,15,0,80,85,3,34,
        17,0,81,85,3,36,18,0,82,85,3,38,19,0,83,85,3,40,20,0,84,74,1,0,0,
        0,84,75,1,0,0,0,84,76,1,0,0,0,84,77,1,0,0,0,84,78,1,0,0,0,84,79,
        1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,
        85,9,1,0,0,0,86,97,5,3,0,0,87,89,5,9,0,0,88,90,5,15,0,0,89,88,1,
        0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,5,3,0,0,92,91,1,0,0,0,92,
        93,1,0,0,0,93,97,1,0,0,0,94,97,5,4,0,0,95,97,5,2,0,0,96,86,1,0,0,
        0,96,87,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,11,1,0,0,0,98,110,
        5,7,0,0,99,100,5,15,0,0,100,101,5,23,0,0,101,110,5,7,0,0,102,104,
        5,7,0,0,103,105,5,21,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,107,
        1,0,0,0,106,108,3,24,12,0,107,106,1,0,0,0,107,108,1,0,0,0,108,110,
        1,0,0,0,109,98,1,0,0,0,109,99,1,0,0,0,109,102,1,0,0,0,110,13,1,0,
        0,0,111,112,5,9,0,0,112,113,5,15,0,0,113,122,5,10,0,0,114,116,5,
        10,0,0,115,117,3,16,8,0,116,115,1,0,0,0,116,117,1,0,0,0,117,122,
        1,0,0,0,118,119,5,3,0,0,119,120,5,15,0,0,120,122,5,9,0,0,121,111,
        1,0,0,0,121,114,1,0,0,0,121,118,1,0,0,0,122,15,1,0,0,0,123,125,5,
        21,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,128,5,
        15,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,132,1,0,0,0,129,130,5,
        21,0,0,130,132,3,24,12,0,131,124,1,0,0,0,131,129,1,0,0,0,132,17,
        1,0,0,0,133,135,3,20,10,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,138,3,22,11,0,137,139,3,24,12,0,138,137,1,0,0,0,138,
        139,1,0,0,0,139,143,1,0,0,0,140,141,5,15,0,0,141,143,3,26,13,0,142,
        134,1,0,0,0,142,140,1,0,0,0,143,19,1,0,0,0,144,152,5,15,0,0,145,
        146,5,14,0,0,146,152,5,24,0,0,147,149,5,20,0,0,148,147,1,0,0,0,148,
        149,1,0,0,0,149,150,1,0,0,0,150,152,5,24,0,0,151,144,1,0,0,0,151,
        145,1,0,0,0,151,148,1,0,0,0,152,21,1,0,0,0,153,154,7,0,0,0,154,23,
        1,0,0,0,155,157,5,20,0,0,156,155,1,0,0,0,156,157,1,0,0,0,157,159,
        1,0,0,0,158,160,5,14,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,162,
        1,0,0,0,161,163,5,24,0,0,162,161,1,0,0,0,163,164,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,168,1,0,0,0,166,168,5,15,0,0,167,156,
        1,0,0,0,167,166,1,0,0,0,168,25,1,0,0,0,169,170,5,23,0,0,170,173,
        3,28,14,0,171,173,3,28,14,0,172,169,1,0,0,0,172,171,1,0,0,0,173,
        27,1,0,0,0,174,175,7,1,0,0,175,29,1,0,0,0,176,177,7,2,0,0,177,31,
        1,0,0,0,178,189,5,16,0,0,179,180,5,9,0,0,180,189,5,15,0,0,181,183,
        5,16,0,0,182,184,5,23,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,186,
        1,0,0,0,185,187,5,15,0,0,186,185,1,0,0,0,186,187,1,0,0,0,187,189,
        1,0,0,0,188,178,1,0,0,0,188,179,1,0,0,0,188,181,1,0,0,0,189,33,1,
        0,0,0,190,191,7,3,0,0,191,35,1,0,0,0,192,199,5,5,0,0,193,199,5,6,
        0,0,194,195,5,19,0,0,195,199,5,11,0,0,196,197,5,19,0,0,197,199,5,
        3,0,0,198,192,1,0,0,0,198,193,1,0,0,0,198,194,1,0,0,0,198,196,1,
        0,0,0,199,37,1,0,0,0,200,201,7,4,0,0,201,39,1,0,0,0,202,203,7,5,
        0,0,203,41,1,0,0,0,35,43,48,51,54,58,62,66,70,72,84,89,92,96,104,
        107,109,116,121,124,127,131,134,138,142,148,151,156,159,164,167,
        172,183,186,188,198
    ]

class SentenceParser ( Parser ):

    grammarFileName = "SentenceParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "GREETING", "THANK_YOU", "SOFT_WORD", 
                      "HEDGE_WORD", "STRONG_WORD", "COMMAND_WORD", "APOLOGY_WORD", 
                      "EMPATHY_WORD", "POLITE_VERB", "REQUEST_WORD", "POSITIVE_ADJ", 
                      "NEGATIVE_EMOTION", "POSITIVE_EMOTION", "POSSESSIVE", 
                      "PRONOUN", "QUESTION_WORD", "TIME_WORD", "CONJUNCTION", 
                      "NEGATION", "ARTICLE", "PREPOSITION", "NUMBER", "COMMON_VERB", 
                      "WORD", "PUNCT", "COMMA", "SEMICOLON", "COLON", "QUOTE", 
                      "EMOTICON", "WS" ]

    RULE_sentence = 0
    RULE_greeting = 1
    RULE_closing = 2
    RULE_polite_closing = 3
    RULE_element = 4
    RULE_polite_phrase = 5
    RULE_apology_phrase = 6
    RULE_request_phrase = 7
    RULE_help_pattern = 8
    RULE_statement_phrase = 9
    RULE_subject_phrase = 10
    RULE_verb_phrase = 11
    RULE_object_phrase = 12
    RULE_feeling_phrase = 13
    RULE_emotional_state = 14
    RULE_emotional_expression = 15
    RULE_question_phrase = 16
    RULE_softener = 17
    RULE_strong_expression = 18
    RULE_basic_word = 19
    RULE_punctuation_element = 20

    ruleNames =  [ "sentence", "greeting", "closing", "polite_closing", 
                   "element", "polite_phrase", "apology_phrase", "request_phrase", 
                   "help_pattern", "statement_phrase", "subject_phrase", 
                   "verb_phrase", "object_phrase", "feeling_phrase", "emotional_state", 
                   "emotional_expression", "question_phrase", "softener", 
                   "strong_expression", "basic_word", "punctuation_element" ]

    EOF = Token.EOF
    GREETING=1
    THANK_YOU=2
    SOFT_WORD=3
    HEDGE_WORD=4
    STRONG_WORD=5
    COMMAND_WORD=6
    APOLOGY_WORD=7
    EMPATHY_WORD=8
    POLITE_VERB=9
    REQUEST_WORD=10
    POSITIVE_ADJ=11
    NEGATIVE_EMOTION=12
    POSITIVE_EMOTION=13
    POSSESSIVE=14
    PRONOUN=15
    QUESTION_WORD=16
    TIME_WORD=17
    CONJUNCTION=18
    NEGATION=19
    ARTICLE=20
    PREPOSITION=21
    NUMBER=22
    COMMON_VERB=23
    WORD=24
    PUNCT=25
    COMMA=26
    SEMICOLON=27
    COLON=28
    QUOTE=29
    EMOTICON=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def greeting(self):
            return self.getTypedRuleContext(SentenceParser.GreetingContext,0)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenceParser.ElementContext)
            else:
                return self.getTypedRuleContext(SentenceParser.ElementContext,i)


        def closing(self):
            return self.getTypedRuleContext(SentenceParser.ClosingContext,0)


        def PUNCT(self):
            return self.getToken(SentenceParser.PUNCT, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_sentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = SentenceParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 42
                self.greeting()


            self.state = 46 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 45
                    self.element()

                else:
                    raise NoViableAltException(self)
                self.state = 48 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140) != 0):
                self.state = 50
                self.closing()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 53
                self.match(SentenceParser.PUNCT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GreetingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREETING(self):
            return self.getToken(SentenceParser.GREETING, 0)

        def COMMA(self):
            return self.getToken(SentenceParser.COMMA, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_greeting

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreeting" ):
                return visitor.visitGreeting(self)
            else:
                return visitor.visitChildren(self)




    def greeting(self):

        localctx = SentenceParser.GreetingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_greeting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SentenceParser.GREETING)
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 57
                self.match(SentenceParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClosingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THANK_YOU(self):
            return self.getToken(SentenceParser.THANK_YOU, 0)

        def polite_closing(self):
            return self.getTypedRuleContext(SentenceParser.Polite_closingContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_closing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosing" ):
                return visitor.visitClosing(self)
            else:
                return visitor.visitChildren(self)




    def closing(self):

        localctx = SentenceParser.ClosingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_closing)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(SentenceParser.THANK_YOU)
                pass
            elif token in [3, 7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.polite_closing()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polite_closingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOFT_WORD(self):
            return self.getToken(SentenceParser.SOFT_WORD, 0)

        def PUNCT(self):
            return self.getToken(SentenceParser.PUNCT, 0)

        def APOLOGY_WORD(self):
            return self.getToken(SentenceParser.APOLOGY_WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_polite_closing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolite_closing" ):
                return visitor.visitPolite_closing(self)
            else:
                return visitor.visitChildren(self)




    def polite_closing(self):

        localctx = SentenceParser.Polite_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_polite_closing)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(SentenceParser.SOFT_WORD)
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 65
                    self.match(SentenceParser.PUNCT)


                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(SentenceParser.APOLOGY_WORD)
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 69
                    self.match(SentenceParser.PUNCT)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def polite_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Polite_phraseContext,0)


        def apology_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Apology_phraseContext,0)


        def request_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Request_phraseContext,0)


        def statement_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Statement_phraseContext,0)


        def question_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Question_phraseContext,0)


        def emotional_expression(self):
            return self.getTypedRuleContext(SentenceParser.Emotional_expressionContext,0)


        def softener(self):
            return self.getTypedRuleContext(SentenceParser.SoftenerContext,0)


        def strong_expression(self):
            return self.getTypedRuleContext(SentenceParser.Strong_expressionContext,0)


        def basic_word(self):
            return self.getTypedRuleContext(SentenceParser.Basic_wordContext,0)


        def punctuation_element(self):
            return self.getTypedRuleContext(SentenceParser.Punctuation_elementContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = SentenceParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.polite_phrase()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.apology_phrase()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.request_phrase()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.statement_phrase()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.question_phrase()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.emotional_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.softener()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.strong_expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 82
                self.basic_word()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 83
                self.punctuation_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polite_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOFT_WORD(self):
            return self.getToken(SentenceParser.SOFT_WORD, 0)

        def POLITE_VERB(self):
            return self.getToken(SentenceParser.POLITE_VERB, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def HEDGE_WORD(self):
            return self.getToken(SentenceParser.HEDGE_WORD, 0)

        def THANK_YOU(self):
            return self.getToken(SentenceParser.THANK_YOU, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_polite_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolite_phrase" ):
                return visitor.visitPolite_phrase(self)
            else:
                return visitor.visitChildren(self)




    def polite_phrase(self):

        localctx = SentenceParser.Polite_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_polite_phrase)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(SentenceParser.SOFT_WORD)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(SentenceParser.POLITE_VERB)
                self.state = 89
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.match(SentenceParser.PRONOUN)


                self.state = 92
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 91
                    self.match(SentenceParser.SOFT_WORD)


                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(SentenceParser.HEDGE_WORD)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.match(SentenceParser.THANK_YOU)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Apology_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APOLOGY_WORD(self):
            return self.getToken(SentenceParser.APOLOGY_WORD, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def COMMON_VERB(self):
            return self.getToken(SentenceParser.COMMON_VERB, 0)

        def PREPOSITION(self):
            return self.getToken(SentenceParser.PREPOSITION, 0)

        def object_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Object_phraseContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_apology_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApology_phrase" ):
                return visitor.visitApology_phrase(self)
            else:
                return visitor.visitChildren(self)




    def apology_phrase(self):

        localctx = SentenceParser.Apology_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_apology_phrase)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(SentenceParser.APOLOGY_WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(SentenceParser.PRONOUN)
                self.state = 100
                self.match(SentenceParser.COMMON_VERB)
                self.state = 101
                self.match(SentenceParser.APOLOGY_WORD)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.match(SentenceParser.APOLOGY_WORD)
                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.match(SentenceParser.PREPOSITION)


                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.object_phrase()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Request_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POLITE_VERB(self):
            return self.getToken(SentenceParser.POLITE_VERB, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def REQUEST_WORD(self):
            return self.getToken(SentenceParser.REQUEST_WORD, 0)

        def help_pattern(self):
            return self.getTypedRuleContext(SentenceParser.Help_patternContext,0)


        def SOFT_WORD(self):
            return self.getToken(SentenceParser.SOFT_WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_request_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequest_phrase" ):
                return visitor.visitRequest_phrase(self)
            else:
                return visitor.visitChildren(self)




    def request_phrase(self):

        localctx = SentenceParser.Request_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_request_phrase)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(SentenceParser.POLITE_VERB)
                self.state = 112
                self.match(SentenceParser.PRONOUN)
                self.state = 113
                self.match(SentenceParser.REQUEST_WORD)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(SentenceParser.REQUEST_WORD)
                self.state = 116
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 115
                    self.help_pattern()


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(SentenceParser.SOFT_WORD)
                self.state = 119
                self.match(SentenceParser.PRONOUN)
                self.state = 120
                self.match(SentenceParser.POLITE_VERB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Help_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPOSITION(self):
            return self.getToken(SentenceParser.PREPOSITION, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def object_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Object_phraseContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_help_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelp_pattern" ):
                return visitor.visitHelp_pattern(self)
            else:
                return visitor.visitChildren(self)




    def help_pattern(self):

        localctx = SentenceParser.Help_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_help_pattern)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 123
                    self.match(SentenceParser.PREPOSITION)


                self.state = 127
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 126
                    self.match(SentenceParser.PRONOUN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(SentenceParser.PREPOSITION)
                self.state = 130
                self.object_phrase()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Verb_phraseContext,0)


        def subject_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Subject_phraseContext,0)


        def object_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Object_phraseContext,0)


        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def feeling_phrase(self):
            return self.getTypedRuleContext(SentenceParser.Feeling_phraseContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_statement_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_phrase" ):
                return visitor.visitStatement_phrase(self)
            else:
                return visitor.visitChildren(self)




    def statement_phrase(self):

        localctx = SentenceParser.Statement_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement_phrase)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 133
                    self.subject_phrase()


                self.state = 136
                self.verb_phrase()
                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 137
                    self.object_phrase()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(SentenceParser.PRONOUN)
                self.state = 141
                self.feeling_phrase()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subject_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def POSSESSIVE(self):
            return self.getToken(SentenceParser.POSSESSIVE, 0)

        def WORD(self):
            return self.getToken(SentenceParser.WORD, 0)

        def ARTICLE(self):
            return self.getToken(SentenceParser.ARTICLE, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_subject_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubject_phrase" ):
                return visitor.visitSubject_phrase(self)
            else:
                return visitor.visitChildren(self)




    def subject_phrase(self):

        localctx = SentenceParser.Subject_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subject_phrase)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(SentenceParser.PRONOUN)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(SentenceParser.POSSESSIVE)
                self.state = 146
                self.match(SentenceParser.WORD)
                pass
            elif token in [20, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 147
                    self.match(SentenceParser.ARTICLE)


                self.state = 150
                self.match(SentenceParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Verb_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMON_VERB(self):
            return self.getToken(SentenceParser.COMMON_VERB, 0)

        def POLITE_VERB(self):
            return self.getToken(SentenceParser.POLITE_VERB, 0)

        def WORD(self):
            return self.getToken(SentenceParser.WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_verb_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb_phrase" ):
                return visitor.visitVerb_phrase(self)
            else:
                return visitor.visitChildren(self)




    def verb_phrase(self):

        localctx = SentenceParser.Verb_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_verb_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25166336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARTICLE(self):
            return self.getToken(SentenceParser.ARTICLE, 0)

        def POSSESSIVE(self):
            return self.getToken(SentenceParser.POSSESSIVE, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SentenceParser.WORD)
            else:
                return self.getToken(SentenceParser.WORD, i)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_object_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_phrase" ):
                return visitor.visitObject_phrase(self)
            else:
                return visitor.visitChildren(self)




    def object_phrase(self):

        localctx = SentenceParser.Object_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_object_phrase)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 20, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 155
                    self.match(SentenceParser.ARTICLE)


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 158
                    self.match(SentenceParser.POSSESSIVE)


                self.state = 162 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 161
                        self.match(SentenceParser.WORD)

                    else:
                        raise NoViableAltException(self)
                    self.state = 164 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(SentenceParser.PRONOUN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feeling_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMON_VERB(self):
            return self.getToken(SentenceParser.COMMON_VERB, 0)

        def emotional_state(self):
            return self.getTypedRuleContext(SentenceParser.Emotional_stateContext,0)


        def getRuleIndex(self):
            return SentenceParser.RULE_feeling_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeeling_phrase" ):
                return visitor.visitFeeling_phrase(self)
            else:
                return visitor.visitChildren(self)




    def feeling_phrase(self):

        localctx = SentenceParser.Feeling_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_feeling_phrase)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(SentenceParser.COMMON_VERB)
                self.state = 170
                self.emotional_state()
                pass
            elif token in [5, 11, 12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.emotional_state()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Emotional_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIVE_EMOTION(self):
            return self.getToken(SentenceParser.POSITIVE_EMOTION, 0)

        def NEGATIVE_EMOTION(self):
            return self.getToken(SentenceParser.NEGATIVE_EMOTION, 0)

        def POSITIVE_ADJ(self):
            return self.getToken(SentenceParser.POSITIVE_ADJ, 0)

        def STRONG_WORD(self):
            return self.getToken(SentenceParser.STRONG_WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_emotional_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmotional_state" ):
                return visitor.visitEmotional_state(self)
            else:
                return visitor.visitChildren(self)




    def emotional_state(self):

        localctx = SentenceParser.Emotional_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_emotional_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Emotional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMPATHY_WORD(self):
            return self.getToken(SentenceParser.EMPATHY_WORD, 0)

        def POSITIVE_EMOTION(self):
            return self.getToken(SentenceParser.POSITIVE_EMOTION, 0)

        def NEGATIVE_EMOTION(self):
            return self.getToken(SentenceParser.NEGATIVE_EMOTION, 0)

        def EMOTICON(self):
            return self.getToken(SentenceParser.EMOTICON, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_emotional_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmotional_expression" ):
                return visitor.visitEmotional_expression(self)
            else:
                return visitor.visitChildren(self)




    def emotional_expression(self):

        localctx = SentenceParser.Emotional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_emotional_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073754368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_WORD(self):
            return self.getToken(SentenceParser.QUESTION_WORD, 0)

        def POLITE_VERB(self):
            return self.getToken(SentenceParser.POLITE_VERB, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def COMMON_VERB(self):
            return self.getToken(SentenceParser.COMMON_VERB, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_question_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion_phrase" ):
                return visitor.visitQuestion_phrase(self)
            else:
                return visitor.visitChildren(self)




    def question_phrase(self):

        localctx = SentenceParser.Question_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_question_phrase)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(SentenceParser.QUESTION_WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(SentenceParser.POLITE_VERB)
                self.state = 180
                self.match(SentenceParser.PRONOUN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(SentenceParser.QUESTION_WORD)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 182
                    self.match(SentenceParser.COMMON_VERB)


                self.state = 186
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 185
                    self.match(SentenceParser.PRONOUN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SoftenerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOFT_WORD(self):
            return self.getToken(SentenceParser.SOFT_WORD, 0)

        def HEDGE_WORD(self):
            return self.getToken(SentenceParser.HEDGE_WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_softener

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoftener" ):
                return visitor.visitSoftener(self)
            else:
                return visitor.visitChildren(self)




    def softener(self):

        localctx = SentenceParser.SoftenerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_softener)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Strong_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRONG_WORD(self):
            return self.getToken(SentenceParser.STRONG_WORD, 0)

        def COMMAND_WORD(self):
            return self.getToken(SentenceParser.COMMAND_WORD, 0)

        def NEGATION(self):
            return self.getToken(SentenceParser.NEGATION, 0)

        def POSITIVE_ADJ(self):
            return self.getToken(SentenceParser.POSITIVE_ADJ, 0)

        def SOFT_WORD(self):
            return self.getToken(SentenceParser.SOFT_WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_strong_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrong_expression" ):
                return visitor.visitStrong_expression(self)
            else:
                return visitor.visitChildren(self)




    def strong_expression(self):

        localctx = SentenceParser.Strong_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_strong_expression)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(SentenceParser.STRONG_WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(SentenceParser.COMMAND_WORD)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(SentenceParser.NEGATION)
                self.state = 195
                self.match(SentenceParser.POSITIVE_ADJ)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(SentenceParser.NEGATION)
                self.state = 197
                self.match(SentenceParser.SOFT_WORD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREETING(self):
            return self.getToken(SentenceParser.GREETING, 0)

        def POSSESSIVE(self):
            return self.getToken(SentenceParser.POSSESSIVE, 0)

        def PRONOUN(self):
            return self.getToken(SentenceParser.PRONOUN, 0)

        def ARTICLE(self):
            return self.getToken(SentenceParser.ARTICLE, 0)

        def PREPOSITION(self):
            return self.getToken(SentenceParser.PREPOSITION, 0)

        def CONJUNCTION(self):
            return self.getToken(SentenceParser.CONJUNCTION, 0)

        def NUMBER(self):
            return self.getToken(SentenceParser.NUMBER, 0)

        def COMMON_VERB(self):
            return self.getToken(SentenceParser.COMMON_VERB, 0)

        def TIME_WORD(self):
            return self.getToken(SentenceParser.TIME_WORD, 0)

        def WORD(self):
            return self.getToken(SentenceParser.WORD, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_basic_word

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_word" ):
                return visitor.visitBasic_word(self)
            else:
                return visitor.visitChildren(self)




    def basic_word(self):

        localctx = SentenceParser.Basic_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_basic_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32948226) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Punctuation_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(SentenceParser.COMMA, 0)

        def SEMICOLON(self):
            return self.getToken(SentenceParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(SentenceParser.COLON, 0)

        def QUOTE(self):
            return self.getToken(SentenceParser.QUOTE, 0)

        def getRuleIndex(self):
            return SentenceParser.RULE_punctuation_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPunctuation_element" ):
                return visitor.visitPunctuation_element(self)
            else:
                return visitor.visitChildren(self)




    def punctuation_element(self):

        localctx = SentenceParser.Punctuation_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_punctuation_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





