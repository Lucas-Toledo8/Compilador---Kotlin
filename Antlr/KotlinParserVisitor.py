# Generated from KotlinParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete generic visitor for a parse tree produced by KotlinParser.

class KotlinParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KotlinParser#kotlinFile.
    def visitKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:KotlinParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#statement.
    def visitStatement(self, ctx:KotlinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#stringLiteral.
    def visitStringLiteral(self, ctx:KotlinParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#declaration.
    def visitDeclaration(self, ctx:KotlinParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#type.
    def visitType(self, ctx:KotlinParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#assignment.
    def visitAssignment(self, ctx:KotlinParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#ifExpression.
    def visitIfExpression(self, ctx:KotlinParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#loopExpression.
    def visitLoopExpression(self, ctx:KotlinParser.LoopExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#block.
    def visitBlock(self, ctx:KotlinParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionCall.
    def visitFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#expression.
    def visitExpression(self, ctx:KotlinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#logicalAnd.
    def visitLogicalAnd(self, ctx:KotlinParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#equality.
    def visitEquality(self, ctx:KotlinParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#comparison.
    def visitComparison(self, ctx:KotlinParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#arithmetic.
    def visitArithmetic(self, ctx:KotlinParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#term.
    def visitTerm(self, ctx:KotlinParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#factor.
    def visitFactor(self, ctx:KotlinParser.FactorContext):
        return self.visitChildren(ctx)



del KotlinParser