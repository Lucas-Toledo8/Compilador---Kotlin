# Generated from KotlinParser.g4 by ANTLR 4.13.2
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
        4,1,35,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,5,0,39,8,0,10,0,
        12,0,42,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,58,8,2,1,3,1,3,3,3,62,8,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,70,
        8,4,1,4,1,4,3,4,74,8,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,93,8,7,3,7,95,8,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,5,9,105,8,9,10,9,12,9,108,9,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,124,8,10,
        1,11,1,11,1,11,5,11,129,8,11,10,11,12,11,132,9,11,1,12,1,12,1,12,
        5,12,137,8,12,10,12,12,12,140,9,12,1,13,1,13,1,13,5,13,145,8,13,
        10,13,12,13,148,9,13,1,14,1,14,1,14,5,14,153,8,14,10,14,12,14,156,
        9,14,1,15,1,15,1,15,5,15,161,8,15,10,15,12,15,164,9,15,1,16,1,16,
        1,16,5,16,169,8,16,10,16,12,16,172,9,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,3,17,181,8,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,0,5,1,0,8,9,1,0,21,22,2,0,19,20,23,24,1,0,25,
        26,1,0,27,28,187,0,40,1,0,0,0,2,45,1,0,0,0,4,57,1,0,0,0,6,59,1,0,
        0,0,8,65,1,0,0,0,10,77,1,0,0,0,12,79,1,0,0,0,14,84,1,0,0,0,16,96,
        1,0,0,0,18,102,1,0,0,0,20,123,1,0,0,0,22,125,1,0,0,0,24,133,1,0,
        0,0,26,141,1,0,0,0,28,149,1,0,0,0,30,157,1,0,0,0,32,165,1,0,0,0,
        34,180,1,0,0,0,36,39,3,2,1,0,37,39,3,4,2,0,38,36,1,0,0,0,38,37,1,
        0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,
        40,1,0,0,0,43,44,5,0,0,1,44,1,1,0,0,0,45,46,5,1,0,0,46,47,5,30,0,
        0,47,48,5,13,0,0,48,49,5,14,0,0,49,50,3,18,9,0,50,3,1,0,0,0,51,58,
        3,8,4,0,52,58,3,12,6,0,53,58,3,16,8,0,54,58,3,14,7,0,55,58,3,20,
        10,0,56,58,3,18,9,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,
        54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,5,1,0,0,0,59,61,5,29,0,
        0,60,62,5,34,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,
        5,35,0,0,64,7,1,0,0,0,65,66,5,2,0,0,66,69,5,30,0,0,67,68,5,11,0,
        0,68,70,3,10,5,0,69,67,1,0,0,0,69,70,1,0,0,0,70,73,1,0,0,0,71,72,
        5,10,0,0,72,74,3,22,11,0,73,71,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,
        0,75,76,5,12,0,0,76,9,1,0,0,0,77,78,7,0,0,0,78,11,1,0,0,0,79,80,
        5,30,0,0,80,81,5,10,0,0,81,82,3,22,11,0,82,83,5,12,0,0,83,13,1,0,
        0,0,84,85,5,3,0,0,85,86,5,13,0,0,86,87,3,22,11,0,87,88,5,14,0,0,
        88,94,3,18,9,0,89,92,5,4,0,0,90,93,3,18,9,0,91,93,3,14,7,0,92,90,
        1,0,0,0,92,91,1,0,0,0,93,95,1,0,0,0,94,89,1,0,0,0,94,95,1,0,0,0,
        95,15,1,0,0,0,96,97,5,5,0,0,97,98,5,13,0,0,98,99,3,22,11,0,99,100,
        5,14,0,0,100,101,3,18,9,0,101,17,1,0,0,0,102,106,5,15,0,0,103,105,
        3,4,2,0,104,103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,
        1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,16,0,0,110,19,
        1,0,0,0,111,112,5,6,0,0,112,113,5,13,0,0,113,114,3,22,11,0,114,115,
        5,14,0,0,115,116,5,12,0,0,116,124,1,0,0,0,117,118,5,30,0,0,118,119,
        5,10,0,0,119,120,5,7,0,0,120,121,5,13,0,0,121,122,5,14,0,0,122,124,
        5,12,0,0,123,111,1,0,0,0,123,117,1,0,0,0,124,21,1,0,0,0,125,130,
        3,24,12,0,126,127,5,18,0,0,127,129,3,24,12,0,128,126,1,0,0,0,129,
        132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,23,1,0,0,0,132,130,
        1,0,0,0,133,138,3,26,13,0,134,135,5,17,0,0,135,137,3,26,13,0,136,
        134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,
        25,1,0,0,0,140,138,1,0,0,0,141,146,3,28,14,0,142,143,7,1,0,0,143,
        145,3,28,14,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,
        147,1,0,0,0,147,27,1,0,0,0,148,146,1,0,0,0,149,154,3,30,15,0,150,
        151,7,2,0,0,151,153,3,30,15,0,152,150,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,29,1,0,0,0,156,154,1,0,0,0,157,162,
        3,32,16,0,158,159,7,3,0,0,159,161,3,32,16,0,160,158,1,0,0,0,161,
        164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,31,1,0,0,0,164,162,
        1,0,0,0,165,170,3,34,17,0,166,167,7,4,0,0,167,169,3,34,17,0,168,
        166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,
        33,1,0,0,0,172,170,1,0,0,0,173,174,5,13,0,0,174,175,3,22,11,0,175,
        176,5,14,0,0,176,181,1,0,0,0,177,181,5,30,0,0,178,181,5,31,0,0,179,
        181,3,6,3,0,180,173,1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,0,180,
        179,1,0,0,0,181,35,1,0,0,0,17,38,40,57,61,69,73,92,94,106,123,130,
        138,146,154,162,170,180
    ]

class KotlinParser ( Parser ):

    grammarFileName = "KotlinParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fun'", "'var'", "'if'", "'else'", "'while'", 
                     "'println'", "'readln'", "'Int'", "'String'", "'='", 
                     "':'", "';'", "'('", "')'", "'{'", "'}'", "'&&'", "'||'", 
                     "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "FUN", "VAR", "IF", "ELSE", "WHILE", 
                      "PRINTLN", "READLN", "INT_TYPE", "STR_TYPE", "ASSIGNMENT", 
                      "COLON", "SEMICOLON", "LPAREN", "RPAREN", "LCURL", 
                      "RCURL", "AND", "OR", "LE", "GE", "EXCL_EQ", "EQEQ", 
                      "LANGLE", "RANGLE", "ADD", "SUB", "MULT", "DIV", "QUOTE_OPEN", 
                      "Identifier", "IntegerLiteral", "WS", "LineComment", 
                      "LineStrText", "QUOTE_CLOSE" ]

    RULE_kotlinFile = 0
    RULE_functionDefinition = 1
    RULE_statement = 2
    RULE_stringLiteral = 3
    RULE_declaration = 4
    RULE_type = 5
    RULE_assignment = 6
    RULE_ifExpression = 7
    RULE_loopExpression = 8
    RULE_block = 9
    RULE_functionCall = 10
    RULE_expression = 11
    RULE_logicalAnd = 12
    RULE_equality = 13
    RULE_comparison = 14
    RULE_arithmetic = 15
    RULE_term = 16
    RULE_factor = 17

    ruleNames =  [ "kotlinFile", "functionDefinition", "statement", "stringLiteral", 
                   "declaration", "type", "assignment", "ifExpression", 
                   "loopExpression", "block", "functionCall", "expression", 
                   "logicalAnd", "equality", "comparison", "arithmetic", 
                   "term", "factor" ]

    EOF = Token.EOF
    FUN=1
    VAR=2
    IF=3
    ELSE=4
    WHILE=5
    PRINTLN=6
    READLN=7
    INT_TYPE=8
    STR_TYPE=9
    ASSIGNMENT=10
    COLON=11
    SEMICOLON=12
    LPAREN=13
    RPAREN=14
    LCURL=15
    RCURL=16
    AND=17
    OR=18
    LE=19
    GE=20
    EXCL_EQ=21
    EQEQ=22
    LANGLE=23
    RANGLE=24
    ADD=25
    SUB=26
    MULT=27
    DIV=28
    QUOTE_OPEN=29
    Identifier=30
    IntegerLiteral=31
    WS=32
    LineComment=33
    LineStrText=34
    QUOTE_CLOSE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class KotlinFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KotlinParser.EOF, 0)

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FunctionDefinitionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_kotlinFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKotlinFile" ):
                listener.enterKotlinFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKotlinFile" ):
                listener.exitKotlinFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKotlinFile" ):
                return visitor.visitKotlinFile(self)
            else:
                return visitor.visitChildren(self)




    def kotlinFile(self):

        localctx = KotlinParser.KotlinFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_kotlinFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073774702) != 0):
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 36
                    self.functionDefinition()
                    pass
                elif token in [2, 3, 5, 6, 15, 30]:
                    self.state = 37
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(KotlinParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(KotlinParser.FUN, 0)

        def Identifier(self):
            return self.getToken(KotlinParser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = KotlinParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(KotlinParser.FUN)
            self.state = 46
            self.match(KotlinParser.Identifier)
            self.state = 47
            self.match(KotlinParser.LPAREN)
            self.state = 48
            self.match(KotlinParser.RPAREN)
            self.state = 49
            self.block()
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

        def declaration(self):
            return self.getTypedRuleContext(KotlinParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(KotlinParser.AssignmentContext,0)


        def loopExpression(self):
            return self.getTypedRuleContext(KotlinParser.LoopExpressionContext,0)


        def ifExpression(self):
            return self.getTypedRuleContext(KotlinParser.IfExpressionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(KotlinParser.FunctionCallContext,0)


        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_statement

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

        localctx = KotlinParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.loopExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.ifExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.functionCall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTE_OPEN(self):
            return self.getToken(KotlinParser.QUOTE_OPEN, 0)

        def QUOTE_CLOSE(self):
            return self.getToken(KotlinParser.QUOTE_CLOSE, 0)

        def LineStrText(self):
            return self.getToken(KotlinParser.LineStrText, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = KotlinParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stringLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(KotlinParser.QUOTE_OPEN)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 60
                self.match(KotlinParser.LineStrText)


            self.state = 63
            self.match(KotlinParser.QUOTE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(KotlinParser.VAR, 0)

        def Identifier(self):
            return self.getToken(KotlinParser.Identifier, 0)

        def SEMICOLON(self):
            return self.getToken(KotlinParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def ASSIGNMENT(self):
            return self.getToken(KotlinParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = KotlinParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(KotlinParser.VAR)
            self.state = 66
            self.match(KotlinParser.Identifier)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 67
                self.match(KotlinParser.COLON)
                self.state = 68
                self.type_()


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 71
                self.match(KotlinParser.ASSIGNMENT)
                self.state = 72
                self.expression()


            self.state = 75
            self.match(KotlinParser.SEMICOLON)
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

        def INT_TYPE(self):
            return self.getToken(KotlinParser.INT_TYPE, 0)

        def STR_TYPE(self):
            return self.getToken(KotlinParser.STR_TYPE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_type

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

        localctx = KotlinParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(KotlinParser.Identifier, 0)

        def ASSIGNMENT(self):
            return self.getToken(KotlinParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(KotlinParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = KotlinParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(KotlinParser.Identifier)
            self.state = 80
            self.match(KotlinParser.ASSIGNMENT)
            self.state = 81
            self.expression()
            self.state = 82
            self.match(KotlinParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(KotlinParser.IF, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.BlockContext)
            else:
                return self.getTypedRuleContext(KotlinParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(KotlinParser.ELSE, 0)

        def ifExpression(self):
            return self.getTypedRuleContext(KotlinParser.IfExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_ifExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpression" ):
                listener.enterIfExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpression" ):
                listener.exitIfExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpression" ):
                return visitor.visitIfExpression(self)
            else:
                return visitor.visitChildren(self)




    def ifExpression(self):

        localctx = KotlinParser.IfExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(KotlinParser.IF)
            self.state = 85
            self.match(KotlinParser.LPAREN)
            self.state = 86
            self.expression()
            self.state = 87
            self.match(KotlinParser.RPAREN)
            self.state = 88
            self.block()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 89
                self.match(KotlinParser.ELSE)
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 90
                    self.block()
                    pass
                elif token in [3]:
                    self.state = 91
                    self.ifExpression()
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


    class LoopExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(KotlinParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_loopExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopExpression" ):
                listener.enterLoopExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopExpression" ):
                listener.exitLoopExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopExpression" ):
                return visitor.visitLoopExpression(self)
            else:
                return visitor.visitChildren(self)




    def loopExpression(self):

        localctx = KotlinParser.LoopExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loopExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(KotlinParser.WHILE)
            self.state = 97
            self.match(KotlinParser.LPAREN)
            self.state = 98
            self.expression()
            self.state = 99
            self.match(KotlinParser.RPAREN)
            self.state = 100
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(KotlinParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(KotlinParser.RCURL, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = KotlinParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(KotlinParser.LCURL)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073774700) != 0):
                self.state = 103
                self.statement()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(KotlinParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(KotlinParser.PRINTLN, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(KotlinParser.SEMICOLON, 0)

        def Identifier(self):
            return self.getToken(KotlinParser.Identifier, 0)

        def ASSIGNMENT(self):
            return self.getToken(KotlinParser.ASSIGNMENT, 0)

        def READLN(self):
            return self.getToken(KotlinParser.READLN, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = KotlinParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionCall)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(KotlinParser.PRINTLN)
                self.state = 112
                self.match(KotlinParser.LPAREN)
                self.state = 113
                self.expression()
                self.state = 114
                self.match(KotlinParser.RPAREN)
                self.state = 115
                self.match(KotlinParser.SEMICOLON)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(KotlinParser.Identifier)
                self.state = 118
                self.match(KotlinParser.ASSIGNMENT)
                self.state = 119
                self.match(KotlinParser.READLN)
                self.state = 120
                self.match(KotlinParser.LPAREN)
                self.state = 121
                self.match(KotlinParser.RPAREN)
                self.state = 122
                self.match(KotlinParser.SEMICOLON)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(KotlinParser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.OR)
            else:
                return self.getToken(KotlinParser.OR, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_expression

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




    def expression(self):

        localctx = KotlinParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.logicalAnd()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 126
                self.match(KotlinParser.OR)
                self.state = 127
                self.logicalAnd()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.EqualityContext)
            else:
                return self.getTypedRuleContext(KotlinParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.AND)
            else:
                return self.getToken(KotlinParser.AND, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_logicalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = KotlinParser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.equality()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 134
                self.match(KotlinParser.AND)
                self.state = 135
                self.equality()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ComparisonContext,i)


        def EQEQ(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.EQEQ)
            else:
                return self.getToken(KotlinParser.EQEQ, i)

        def EXCL_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.EXCL_EQ)
            else:
                return self.getToken(KotlinParser.EXCL_EQ, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = KotlinParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.comparison()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.comparison()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ArithmeticContext,i)


        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.LE)
            else:
                return self.getToken(KotlinParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.GE)
            else:
                return self.getToken(KotlinParser.GE, i)

        def LANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.LANGLE)
            else:
                return self.getToken(KotlinParser.LANGLE, i)

        def RANGLE(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.RANGLE)
            else:
                return self.getToken(KotlinParser.RANGLE, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = KotlinParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.arithmetic()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26738688) != 0):
                self.state = 150
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26738688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.arithmetic()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.TermContext)
            else:
                return self.getTypedRuleContext(KotlinParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.ADD)
            else:
                return self.getToken(KotlinParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.SUB)
            else:
                return self.getToken(KotlinParser.SUB, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = KotlinParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.term()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.term()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FactorContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.MULT)
            else:
                return self.getToken(KotlinParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.DIV)
            else:
                return self.getToken(KotlinParser.DIV, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = KotlinParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.factor()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 166
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 167
                self.factor()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def Identifier(self):
            return self.getToken(KotlinParser.Identifier, 0)

        def IntegerLiteral(self):
            return self.getToken(KotlinParser.IntegerLiteral, 0)

        def stringLiteral(self):
            return self.getTypedRuleContext(KotlinParser.StringLiteralContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = KotlinParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(KotlinParser.LPAREN)
                self.state = 174
                self.expression()
                self.state = 175
                self.match(KotlinParser.RPAREN)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(KotlinParser.Identifier)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(KotlinParser.IntegerLiteral)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.stringLiteral()
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





