# Generated from Grammar.g4 by ANTLR 4.13.1
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
        4,1,37,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,
        26,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,37,8,1,10,1,12,1,
        40,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,1,1,
        1,1,1,1,1,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,71,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,82,
        8,1,1,1,1,1,1,1,1,1,3,1,88,8,1,1,1,1,1,1,1,3,1,93,8,1,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,103,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,126,8,
        3,10,3,12,3,129,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,140,
        8,4,1,4,0,1,6,5,0,2,4,6,8,0,5,1,0,23,26,1,0,9,11,2,0,7,7,12,13,1,
        0,14,15,1,0,16,17,166,0,13,1,0,0,0,2,92,1,0,0,0,4,94,1,0,0,0,6,102,
        1,0,0,0,8,139,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,
        13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,
        0,0,1,17,1,1,0,0,0,18,93,5,1,0,0,19,24,3,4,2,0,20,21,5,37,0,0,21,
        23,5,2,0,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,37,0,0,28,29,5,1,0,0,29,93,
        1,0,0,0,30,31,3,6,3,0,31,32,5,1,0,0,32,93,1,0,0,0,33,38,5,27,0,0,
        34,35,5,37,0,0,35,37,5,2,0,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,
        0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,37,0,0,42,
        93,5,1,0,0,43,49,5,28,0,0,44,45,3,6,3,0,45,46,5,2,0,0,46,48,1,0,
        0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,
        1,0,0,0,51,49,1,0,0,0,52,53,3,6,3,0,53,54,5,1,0,0,54,93,1,0,0,0,
        55,59,5,3,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,
        0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,93,5,4,0,0,63,
        64,5,29,0,0,64,65,5,5,0,0,65,66,3,6,3,0,66,67,5,6,0,0,67,70,3,2,
        1,0,68,69,5,30,0,0,69,71,3,2,1,0,70,68,1,0,0,0,70,71,1,0,0,0,71,
        93,1,0,0,0,72,73,5,31,0,0,73,74,5,5,0,0,74,75,3,6,3,0,75,76,5,6,
        0,0,76,77,3,2,1,0,77,93,1,0,0,0,78,79,5,32,0,0,79,81,5,5,0,0,80,
        82,3,6,3,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,5,1,0,
        0,84,85,3,6,3,0,85,87,5,1,0,0,86,88,3,6,3,0,87,86,1,0,0,0,87,88,
        1,0,0,0,88,89,1,0,0,0,89,90,5,6,0,0,90,91,3,2,1,0,91,93,1,0,0,0,
        92,18,1,0,0,0,92,19,1,0,0,0,92,30,1,0,0,0,92,33,1,0,0,0,92,43,1,
        0,0,0,92,55,1,0,0,0,92,63,1,0,0,0,92,72,1,0,0,0,92,78,1,0,0,0,93,
        3,1,0,0,0,94,95,7,0,0,0,95,5,1,0,0,0,96,97,6,3,-1,0,97,103,3,8,4,
        0,98,99,5,7,0,0,99,103,3,6,3,9,100,101,5,8,0,0,101,103,3,6,3,8,102,
        96,1,0,0,0,102,98,1,0,0,0,102,100,1,0,0,0,103,127,1,0,0,0,104,105,
        10,7,0,0,105,106,7,1,0,0,106,126,3,6,3,8,107,108,10,6,0,0,108,109,
        7,2,0,0,109,126,3,6,3,7,110,111,10,5,0,0,111,112,7,3,0,0,112,126,
        3,6,3,6,113,114,10,4,0,0,114,115,7,4,0,0,115,126,3,6,3,5,116,117,
        10,3,0,0,117,118,5,18,0,0,118,126,3,6,3,4,119,120,10,2,0,0,120,121,
        5,19,0,0,121,126,3,6,3,3,122,123,10,1,0,0,123,124,5,20,0,0,124,126,
        3,6,3,1,125,104,1,0,0,0,125,107,1,0,0,0,125,110,1,0,0,0,125,113,
        1,0,0,0,125,116,1,0,0,0,125,119,1,0,0,0,125,122,1,0,0,0,126,129,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,7,1,0,0,0,129,127,1,
        0,0,0,130,131,5,5,0,0,131,132,3,6,3,0,132,133,5,6,0,0,133,140,1,
        0,0,0,134,140,5,36,0,0,135,140,5,35,0,0,136,140,5,33,0,0,137,140,
        5,34,0,0,138,140,5,37,0,0,139,130,1,0,0,0,139,134,1,0,0,0,139,135,
        1,0,0,0,139,136,1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,9,1,
        0,0,0,13,13,24,38,49,59,70,81,87,92,102,125,127,139
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'{'", "'}'", "'('", "')'", 
                     "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", 
                     "'>'", "'=='", "'!='", "'&&'", "'||'", "'='", "<INVALID>", 
                     "<INVALID>", "'int'", "'float'", "'bool'", "'string'", 
                     "'read'", "'write'", "'if'", "'else'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LINE_COMMENT", "WS", "INT", "FLOAT", 
                      "BOOL", "STRING", "READ", "WRITE", "IF", "ELSE", "WHILE", 
                      "FOR", "BOOL_LIT", "STRING_LIT", "FLOAT_LIT", "INT_LIT", 
                      "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_type = 2
    RULE_expression = 3
    RULE_primary = 4

    ruleNames =  [ "program", "statement", "type", "expression", "primary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    LINE_COMMENT=21
    WS=22
    INT=23
    FLOAT=24
    BOOL=25
    STRING=26
    READ=27
    WRITE=28
    IF=29
    ELSE=30
    WHILE=31
    FOR=32
    BOOL_LIT=33
    STRING_LIT=34
    FLOAT_LIT=35
    INT_LIT=36
    ID=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 273795776938) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ID)
            else:
                return self.getToken(GrammarParser.ID, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def READ(self):
            return self.getToken(GrammarParser.READ, 0)

        def WRITE(self):
            return self.getToken(GrammarParser.WRITE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def IF(self):
            return self.getToken(GrammarParser.IF, 0)

        def ELSE(self):
            return self.getToken(GrammarParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(GrammarParser.WHILE, 0)

        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(GrammarParser.T__0)
                pass
            elif token in [23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.type_()
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 20
                        self.match(GrammarParser.ID)
                        self.state = 21
                        self.match(GrammarParser.T__1) 
                    self.state = 26
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 27
                self.match(GrammarParser.ID)
                self.state = 28
                self.match(GrammarParser.T__0)
                pass
            elif token in [5, 7, 8, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.expression(0)
                self.state = 31
                self.match(GrammarParser.T__0)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.match(GrammarParser.READ)
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 34
                        self.match(GrammarParser.ID)
                        self.state = 35
                        self.match(GrammarParser.T__1) 
                    self.state = 40
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 41
                self.match(GrammarParser.ID)
                self.state = 42
                self.match(GrammarParser.T__0)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(GrammarParser.WRITE)
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 44
                        self.expression(0)
                        self.state = 45
                        self.match(GrammarParser.T__1) 
                    self.state = 51
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 52
                self.expression(0)
                self.state = 53
                self.match(GrammarParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.match(GrammarParser.T__2)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 273795776938) != 0):
                    self.state = 56
                    self.statement()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(GrammarParser.T__3)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.match(GrammarParser.IF)
                self.state = 64
                self.match(GrammarParser.T__4)
                self.state = 65
                self.expression(0)
                self.state = 66
                self.match(GrammarParser.T__5)
                self.state = 67
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 68
                    self.match(GrammarParser.ELSE)
                    self.state = 69
                    self.statement()


                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.match(GrammarParser.WHILE)
                self.state = 73
                self.match(GrammarParser.T__4)
                self.state = 74
                self.expression(0)
                self.state = 75
                self.match(GrammarParser.T__5)
                self.state = 76
                self.statement()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.match(GrammarParser.FOR)
                self.state = 79
                self.match(GrammarParser.T__4)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266287972768) != 0):
                    self.state = 80
                    self.expression(0)


                self.state = 83
                self.match(GrammarParser.T__0)
                self.state = 84
                self.expression(0)
                self.state = 85
                self.match(GrammarParser.T__0)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266287972768) != 0):
                    self.state = 86
                    self.expression(0)


                self.state = 89
                self.match(GrammarParser.T__5)
                self.state = 90
                self.statement()
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(GrammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.uop = None # Token
            self.bop = None # Token

        def primary(self):
            return self.getTypedRuleContext(GrammarParser.PrimaryContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 33, 34, 35, 36, 37]:
                self.state = 97
                self.primary()
                pass
            elif token in [7]:
                self.state = 98
                localctx.uop = self.match(GrammarParser.T__6)
                self.state = 99
                self.expression(9)
                pass
            elif token in [8]:
                self.state = 100
                localctx.uop = self.match(GrammarParser.T__7)
                self.state = 101
                self.expression(8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 105
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 108
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12416) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 111
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 114
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 117
                        localctx.bop = self.match(GrammarParser.T__17)
                        self.state = 118
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 120
                        localctx.bop = self.match(GrammarParser.T__18)
                        self.state = 121
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 123
                        localctx.bop = self.match(GrammarParser.T__19)
                        self.state = 124
                        self.expression(1)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def INT_LIT(self):
            return self.getToken(GrammarParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(GrammarParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(GrammarParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(GrammarParser.STRING_LIT, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = GrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primary)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(GrammarParser.T__4)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(GrammarParser.T__5)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(GrammarParser.INT_LIT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(GrammarParser.FLOAT_LIT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(GrammarParser.BOOL_LIT)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.match(GrammarParser.STRING_LIT)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.match(GrammarParser.ID)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




