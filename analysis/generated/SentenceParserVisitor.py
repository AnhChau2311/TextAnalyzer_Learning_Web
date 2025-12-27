# Generated from /Users/anhchau/Documents/Principles of Programming Languages/TextAnalyzer_Learning_Web/analysis/grammar/SentenceParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SentenceParser import SentenceParser
else:
    from SentenceParser import SentenceParser

# This class defines a complete generic visitor for a parse tree produced by SentenceParser.

class SentenceParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SentenceParser#sentence.
    def visitSentence(self, ctx:SentenceParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#greeting.
    def visitGreeting(self, ctx:SentenceParser.GreetingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#closing.
    def visitClosing(self, ctx:SentenceParser.ClosingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#polite_closing.
    def visitPolite_closing(self, ctx:SentenceParser.Polite_closingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#element.
    def visitElement(self, ctx:SentenceParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#polite_phrase.
    def visitPolite_phrase(self, ctx:SentenceParser.Polite_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#apology_phrase.
    def visitApology_phrase(self, ctx:SentenceParser.Apology_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#request_phrase.
    def visitRequest_phrase(self, ctx:SentenceParser.Request_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#help_pattern.
    def visitHelp_pattern(self, ctx:SentenceParser.Help_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#statement_phrase.
    def visitStatement_phrase(self, ctx:SentenceParser.Statement_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#subject_phrase.
    def visitSubject_phrase(self, ctx:SentenceParser.Subject_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#verb_phrase.
    def visitVerb_phrase(self, ctx:SentenceParser.Verb_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#object_phrase.
    def visitObject_phrase(self, ctx:SentenceParser.Object_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#feeling_phrase.
    def visitFeeling_phrase(self, ctx:SentenceParser.Feeling_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#emotional_state.
    def visitEmotional_state(self, ctx:SentenceParser.Emotional_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#emotional_expression.
    def visitEmotional_expression(self, ctx:SentenceParser.Emotional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#question_phrase.
    def visitQuestion_phrase(self, ctx:SentenceParser.Question_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#softener.
    def visitSoftener(self, ctx:SentenceParser.SoftenerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#strong_expression.
    def visitStrong_expression(self, ctx:SentenceParser.Strong_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#basic_word.
    def visitBasic_word(self, ctx:SentenceParser.Basic_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenceParser#punctuation_element.
    def visitPunctuation_element(self, ctx:SentenceParser.Punctuation_elementContext):
        return self.visitChildren(ctx)



del SentenceParser