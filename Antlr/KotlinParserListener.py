# Generated from KotlinParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete listener for a parse tree produced by KotlinParser.
class KotlinParserListener(ParseTreeListener):

    # Enter a parse tree produced by KotlinParser#kotlinFile.
    def enterKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        pass

    # Exit a parse tree produced by KotlinParser#kotlinFile.
    def exitKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:KotlinParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:KotlinParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by KotlinParser#statement.
    def enterStatement(self, ctx:KotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#statement.
    def exitStatement(self, ctx:KotlinParser.StatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#stringLiteral.
    def enterStringLiteral(self, ctx:KotlinParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#stringLiteral.
    def exitStringLiteral(self, ctx:KotlinParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by KotlinParser#declaration.
    def enterDeclaration(self, ctx:KotlinParser.DeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#declaration.
    def exitDeclaration(self, ctx:KotlinParser.DeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#type.
    def enterType(self, ctx:KotlinParser.TypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#type.
    def exitType(self, ctx:KotlinParser.TypeContext):
        pass


    # Enter a parse tree produced by KotlinParser#assignment.
    def enterAssignment(self, ctx:KotlinParser.AssignmentContext):
        pass

    # Exit a parse tree produced by KotlinParser#assignment.
    def exitAssignment(self, ctx:KotlinParser.AssignmentContext):
        pass


    # Enter a parse tree produced by KotlinParser#ifExpression.
    def enterIfExpression(self, ctx:KotlinParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifExpression.
    def exitIfExpression(self, ctx:KotlinParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#loopExpression.
    def enterLoopExpression(self, ctx:KotlinParser.LoopExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#loopExpression.
    def exitLoopExpression(self, ctx:KotlinParser.LoopExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#block.
    def enterBlock(self, ctx:KotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#block.
    def exitBlock(self, ctx:KotlinParser.BlockContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionCall.
    def enterFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionCall.
    def exitFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by KotlinParser#expression.
    def enterExpression(self, ctx:KotlinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#expression.
    def exitExpression(self, ctx:KotlinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#logicalAnd.
    def enterLogicalAnd(self, ctx:KotlinParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by KotlinParser#logicalAnd.
    def exitLogicalAnd(self, ctx:KotlinParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by KotlinParser#equality.
    def enterEquality(self, ctx:KotlinParser.EqualityContext):
        pass

    # Exit a parse tree produced by KotlinParser#equality.
    def exitEquality(self, ctx:KotlinParser.EqualityContext):
        pass


    # Enter a parse tree produced by KotlinParser#comparison.
    def enterComparison(self, ctx:KotlinParser.ComparisonContext):
        pass

    # Exit a parse tree produced by KotlinParser#comparison.
    def exitComparison(self, ctx:KotlinParser.ComparisonContext):
        pass


    # Enter a parse tree produced by KotlinParser#arithmetic.
    def enterArithmetic(self, ctx:KotlinParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by KotlinParser#arithmetic.
    def exitArithmetic(self, ctx:KotlinParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by KotlinParser#term.
    def enterTerm(self, ctx:KotlinParser.TermContext):
        pass

    # Exit a parse tree produced by KotlinParser#term.
    def exitTerm(self, ctx:KotlinParser.TermContext):
        pass


    # Enter a parse tree produced by KotlinParser#factor.
    def enterFactor(self, ctx:KotlinParser.FactorContext):
        pass

    # Exit a parse tree produced by KotlinParser#factor.
    def exitFactor(self, ctx:KotlinParser.FactorContext):
        pass



del KotlinParser