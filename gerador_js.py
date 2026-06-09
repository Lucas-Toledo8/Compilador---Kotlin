# javascript_generator.py
# Fase de geracao de codigo: Kotlin -> JavaScript

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "Antlr"))

from Antlr.KotlinParserVisitor import KotlinParserVisitor


class JavaScriptGenerator(KotlinParserVisitor):
    """
    Gerador de codigo JavaScript a partir da arvore sintatica do ANTLR.

    Entrada: parse tree gerada por KotlinParser.kotlinFile()
    Saida: codigo JavaScript em string
    """

    def __init__(self, symbols=None):
        super().__init__()
        self.lines = []
        self.indent_level = 0
        self.symbols = symbols or {}

    def indent(self):
        return "    " * self.indent_level

    def emit(self, line=""):
        self.lines.append(self.indent() + line)

    def get_code(self):
        return "\n".join(self.lines)

    def get_symbol_type(self, name):
        symbol = self.symbols.get(name)

        if symbol is None:
            return None

        if hasattr(symbol, "type"):
            return symbol.type

        if isinstance(symbol, dict):
            return symbol.get("type")

        return None

    def emit_block_content(self, block_ctx):
        self.indent_level += 1

        for statement in block_ctx.statement():
            self.visit(statement)

        self.indent_level -= 1

    def visitKotlinFile(self, ctx):
        for child in ctx.getChildren():
            if child.getText() == "<EOF>":
                continue
            self.visit(child)

        return self.get_code()

    def visitFunctionDefinition(self, ctx):
        name = ctx.Identifier().getText()

        self.emit(f"function {name}() {{")
        self.emit_block_content(ctx.block())
        self.emit("}")

        if name == "main":
            self.emit("")
            self.emit("main();")

        return None

    def visitBlock(self, ctx):
        self.emit("{")
        self.emit_block_content(ctx)
        self.emit("}")
        return None

    def visitDeclaration(self, ctx):
        name = ctx.Identifier().getText()

        if ctx.expression():
            expr = self.visit(ctx.expression())
            self.emit(f"let {name} = {expr};")
        else:
            self.emit(f"let {name};")

        return None

    def visitAssignment(self, ctx):
        name = ctx.Identifier().getText()
        expr = self.visit(ctx.expression())

        self.emit(f"{name} = {expr};")

        return None

    def visitFunctionCall(self, ctx):
        if ctx.PRINTLN():
            expr = self.visit(ctx.expression())
            self.emit(f"console.log({expr});")
            return None

        if ctx.READLN():
            name = ctx.Identifier().getText()
            var_type = self.get_symbol_type(name)

            if var_type == "Int":
                self.emit(f'{name} = Number(prompt(""));')
            else:
                self.emit(f'{name} = prompt("");')

            return None

        return None

    def visitLoopExpression(self, ctx):
        cond = self.visit(ctx.expression())

        self.emit(f"while ({cond}) {{")
        self.emit_block_content(ctx.block())
        self.emit("}")

        return None

    def visitIfExpression(self, ctx):
        self.emit_if_chain(ctx, first=True)
        return None

    def emit_if_chain(self, ctx, first=True):
        cond = self.visit(ctx.expression())

        if first:
            self.emit(f"if ({cond}) {{")
        else:
            self.emit(f"}} else if ({cond}) {{")

        self.emit_block_content(ctx.block(0))

        if ctx.ELSE():
            if ctx.ifExpression():
                self.emit_if_chain(ctx.ifExpression(), first=False)
            elif len(ctx.block()) > 1:
                self.emit("} else {")
                self.emit_block_content(ctx.block(1))
                self.emit("}")
            else:
                self.emit("}")
        else:
            self.emit("}")

    def visitExpression(self, ctx):
        result = self.visit(ctx.logicalAnd(0))

        for i in range(1, len(ctx.logicalAnd())):
            right = self.visit(ctx.logicalAnd(i))
            result = f"{result} || {right}"

        return result

    def visitLogicalAnd(self, ctx):
        result = self.visit(ctx.equality(0))

        for i in range(1, len(ctx.equality())):
            right = self.visit(ctx.equality(i))
            result = f"{result} && {right}"

        return result

    def visitEquality(self, ctx):
        result = self.visit(ctx.comparison(0))

        for i in range(1, len(ctx.comparison())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.comparison(i))
            result = f"{result} {op} {right}"

        return result

    def visitComparison(self, ctx):
        result = self.visit(ctx.arithmetic(0))

        for i in range(1, len(ctx.arithmetic())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.arithmetic(i))
            result = f"{result} {op} {right}"

        return result

    def visitArithmetic(self, ctx):
        result = self.visit(ctx.term(0))

        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.term(i))
            result = f"{result} {op} {right}"

        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))
            result = f"{result} {op} {right}"

        return result

    def visitFactor(self, ctx):
        if ctx.IntegerLiteral():
            return ctx.IntegerLiteral().getText()

        if ctx.Identifier():
            return ctx.Identifier().getText()

        if ctx.stringLiteral():
            return self.visit(ctx.stringLiteral())

        if ctx.expression():
            expr = self.visit(ctx.expression())
            return f"({expr})"

        return "undefined"

    def visitStringLiteral(self, ctx):
        return ctx.getText()
