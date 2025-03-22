# Generated from Scheduler.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\6\13P\n\13")
        buf.write("\r\13\16\13Q\3\13\7\13U\n\13\f\13\16\13X\13\13\7\13Z\n")
        buf.write("\13\f\13\16\13]\13\13\3\f\6\f`\n\f\r\f\16\fa\3\f\3\f\2")
        buf.write("\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2h\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\3\31\3\2\2\2\5 \3\2\2\2\7\'\3\2\2\2\t")
        buf.write(",\3\2\2\2\13\60\3\2\2\2\r\66\3\2\2\2\17;\3\2\2\2\21?\3")
        buf.write("\2\2\2\23E\3\2\2\2\25O\3\2\2\2\27_\3\2\2\2\31\32\7\u00c6")
        buf.write("\2\2\32\33\7\u201a\2\2\33\34\7\u00e3\2\2\34\35\7\u00bc")
        buf.write("\2\2\35\36\7\u00b9\2\2\36\37\7v\2\2\37\4\3\2\2\2 !\7n")
        buf.write("\2\2!\"\7\u00e3\2\2\"#\7\u00bd\2\2#$\7\u203b\2\2$%\7e")
        buf.write("\2\2%&\7j\2\2&\6\3\2\2\2\'(\7n\2\2()\7\u00c5\2\2)*\7\u00bc")
        buf.write("\2\2*+\7e\2\2+\b\3\2\2\2,-\7e\2\2-.\7j\2\2./\7q\2\2/\n")
        buf.write("\3\2\2\2\60\61\7p\2\2\61\62\7i\2\2\62\63\7\u00c5\2\2\63")
        buf.write("\64\7\u00a2\2\2\64\65\7{\2\2\65\f\3\2\2\2\66\67\7j\2\2")
        buf.write("\678\7\u00c5\2\289\7\u00b6\2\29:\7o\2\2:\16\3\2\2\2;<")
        buf.write("\7p\2\2<=\7c\2\2=>\7{\2\2>\20\3\2\2\2?@\t\2\2\2@A\b\t")
        buf.write("\2\2AB\7<\2\2BC\t\2\2\2CD\b\t\3\2D\22\3\2\2\2EF\t\2\2")
        buf.write("\2FG\b\n\4\2GH\7\61\2\2HI\t\2\2\2IJ\b\n\5\2JK\7\61\2\2")
        buf.write("KL\t\2\2\2LM\b\n\6\2M\24\3\2\2\2NP\n\3\2\2ON\3\2\2\2P")
        buf.write("Q\3\2\2\2QO\3\2\2\2QR\3\2\2\2R[\3\2\2\2SU\n\3\2\2TS\3")
        buf.write("\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WZ\3\2\2\2XV\3\2\2")
        buf.write("\2YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\26\3\2\2")
        buf.write("\2][\3\2\2\2^`\t\3\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2a")
        buf.write("b\3\2\2\2bc\3\2\2\2cd\b\f\7\2d\30\3\2\2\2\7\2QV[a\b\3")
        buf.write("\t\2\3\t\3\3\n\4\3\n\5\3\n\6\b\2\2")
        return buf.getvalue()


class SchedulerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    TIME = 8
    DATE = 9
    TEXT = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\u00C4\u2018\u00E1\u00BA\u00B7t'", "'l\u00E1\u00BB\u2039ch'", 
            "'l\u00C3\u00BAc'", "'cho'", "'ng\u00C3\u00A0y'", "'h\u00C3\u00B4m'", 
            "'nay'" ]

    symbolicNames = [ "<INVALID>",
            "TIME", "DATE", "TEXT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "TIME", "DATE", "TEXT", "WS" ]

    grammarFileName = "Scheduler.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.TIME_action 
            actions[8] = self.DATE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def TIME_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            1,2
     

        if actionIndex == 1:
            2
     

    def DATE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            1,2
     

        if actionIndex == 3:
            1,2
     

        if actionIndex == 4:
            4
     


