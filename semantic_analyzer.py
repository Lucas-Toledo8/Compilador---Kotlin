# semantic_analyzer.py

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "Antlr"))

from Antlr.KotlinParser import KotlinParser
from Antlr.KotlinParserVisitor import KotlinParserVisitor


class Symbol:
    def __init__(self, name, type_, value=None, line=0, column=0):
        self.name = name
        self.type = type_
        self.value = value
        self.line = line
        self.column = column


class SemanticAnalyzer(KotlinParserVisitor):

    def __init__(self):
        super().__init__()
        self.symbols = {}
        self.errors = []
        self.log = []
        self.logs = self.log

    def semantic_error(self, ctx, msg):
        token = ctx.start
        self.errors.append(
            f"[ERRO SEMANTICO] linha {token.line}, coluna {token.column} - {msg}"
        )

    def visitKotlinFile(self, ctx):
        self.log.append("[SEMANTICO] Visitando arquivo Kotlin")
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx):
        name = ctx.Identifier().getText()
        line = ctx.Identifier().symbol.line
        column = ctx.Identifier().symbol.column

        self.log.append(f"[SEMANTICO] Declarando variavel '{name}'")

        if name in self.symbols:
            self.errors.append(
                f"[ERRO SEMANTICO] linha {line}, coluna {column} - Variavel '{name}' ja declarada."
            )
            return None

        type_ = "Unknown"
        if ctx.type_():
            type_ = ctx.type_().getText()

        value = None
        expr_type = None

        if ctx.expression():
            expr_type, value = self.visit(ctx.expression())

            if expr_type != "Unknown" and type_ != expr_type:
                self.semantic_error(
                    ctx,
                    f"Tipo incompativel na declaracao de '{name}'. Esperado {type_}, recebido {expr_type}."
                )

        self.symbols[name] = Symbol(name, type_, value, line, column)

        self.log.append(
            f"[SEMANTICO] Variavel '{name}' registrada com tipo {type_} e valor {value}"
        )

        return None

    def visitAssignment(self, ctx):
        name = ctx.Identifier().getText()

        self.log.append(f"[SEMANTICO] Atribuindo valor para '{name}'")

        if name not in self.symbols:
            self.semantic_error(ctx, f"Variavel '{name}' usada sem declaracao previa.")
            return None

        expr_type, value = self.visit(ctx.expression())
        var_type = self.symbols[name].type

        if expr_type != "Unknown" and var_type != expr_type:
            self.semantic_error(
                ctx,
                f"Tipo incompativel na atribuicao de '{name}'. Esperado {var_type}, recebido {expr_type}."
            )

        self.symbols[name].value = value

        self.log.append(
            f"[SEMANTICO] Variavel '{name}' atualizada com valor {value}"
        )

        return None

    def visitIfExpression(self, ctx):
        self.log.append("[SEMANTICO] Verificando comando if")

        cond_type, _ = self.visit(ctx.expression())

        if cond_type != "Boolean":
            self.semantic_error(ctx, "Condicao do if deve ser Boolean.")

        for block in ctx.block():
            self.visit(block)

        if ctx.ifExpression():
            self.visit(ctx.ifExpression())

        return None

    def visitLoopExpression(self, ctx):
        self.log.append("[SEMANTICO] Verificando comando while")

        cond_type, _ = self.visit(ctx.expression())

        if cond_type != "Boolean":
            self.semantic_error(ctx, "Condicao do while deve ser Boolean.")

        self.visit(ctx.block())

        return None

    def visitFunctionCall(self, ctx):
        self.log.append("[SEMANTICO] Verificando chamada de funcao")

        if ctx.PRINTLN():
            self.visit(ctx.expression())

        elif ctx.READLN():
            name = ctx.Identifier().getText()

            if name not in self.symbols:
                self.semantic_error(ctx, f"Variavel '{name}' usada sem declaracao previa.")
            else:
                self.symbols[name].value = None
                self.log.append(
                    f"[SEMANTICO] Variavel '{name}' recebeu valor desconhecido via readln()"
                )

        return None

    def visitExpression(self, ctx):
        result_type, result_value = self.visit(ctx.logicalAnd(0))

        for i in range(1, len(ctx.logicalAnd())):
            right_type, right_value = self.visit(ctx.logicalAnd(i))

            self.log.append("[SEMANTICO] Verificando operador logico ||")

            if result_type != "Boolean" or right_type != "Boolean":
                self.semantic_error(ctx, "Operacao logica '||' exige operandos Boolean.")

            result_type = "Boolean"
            result_value = None

        return result_type, result_value

    def visitLogicalAnd(self, ctx):
        result_type, result_value = self.visit(ctx.equality(0))

        for i in range(1, len(ctx.equality())):
            right_type, right_value = self.visit(ctx.equality(i))

            self.log.append("[SEMANTICO] Verificando operador logico &&")

            if result_type != "Boolean" or right_type != "Boolean":
                self.semantic_error(ctx, "Operacao logica '&&' exige operandos Boolean.")

            result_type = "Boolean"
            result_value = None

        return result_type, result_value

    def visitEquality(self, ctx):
        result_type, result_value = self.visit(ctx.comparison(0))

        for i in range(1, len(ctx.comparison())):
            right_type, right_value = self.visit(ctx.comparison(i))

            self.log.append("[SEMANTICO] Verificando operador de igualdade")

            if result_type != right_type:
                self.semantic_error(ctx, "Comparacao exige operandos do mesmo tipo.")

            result_type = "Boolean"
            result_value = None

        return result_type, result_value

    def visitComparison(self, ctx):
        result_type, result_value = self.visit(ctx.arithmetic(0))

        for i in range(1, len(ctx.arithmetic())):
            right_type, right_value = self.visit(ctx.arithmetic(i))

            self.log.append("[SEMANTICO] Verificando operador relacional")

            if result_type != "Int" or right_type != "Int":
                self.semantic_error(ctx, "Operacao relacional exige operandos Int.")

            result_type = "Boolean"
            result_value = None

        return result_type, result_value

    def visitArithmetic(self, ctx):
        result_type, result_value = self.visit(ctx.term(0))

        terms = ctx.term()

        for i in range(1, len(terms)):
            right_type, right_value = self.visit(terms[i])

            op = ctx.getChild(2 * i - 1).getText()

            self.log.append(f"[SEMANTICO] Verificando operacao aritmetica '{op}'")

            if result_type != "Int" or right_type != "Int":
                self.semantic_error(
                 ctx,
                 f"Operacao matematica '{op}' exige operandos Int."
            )

             # Importante:
             # nao tenta calcular expressao com tipos invalidos
                result_type = "Erro"
                result_value = None
                continue

            if result_value is not None and right_value is not None:
                if op == "+":
                    result_value = result_value + right_value
                elif op == "-":
                    result_value = result_value - right_value
                else:
                    result_value = None
            else:
                result_value = None

            result_type = "Int"

        return result_type, result_value

    def visitTerm(self, ctx):
        result_type, result_value = self.visit(ctx.factor(0))

        factors = ctx.factor()

        for i in range(1, len(factors)):
            right_type, right_value = self.visit(factors[i])

            op = ctx.getChild(2 * i - 1).getText()

            self.log.append(f"[SEMANTICO] Verificando operacao termo '{op}'")

            if result_type != "Int" or right_type != "Int":
                self.semantic_error(ctx, f"Operacao matematica '{op}' exige operandos Int.")

            if op == "/" and right_value == 0:
                self.semantic_error(ctx, "Divisao por zero.")

            if result_value is not None and right_value is not None:
                if op == "*":
                    result_value = result_value * right_value
                elif op == "/":
                    if right_value != 0:
                        result_value = result_value // right_value
                    else:
                        result_value = None
            else:
                result_value = None

            result_type = "Int"

        return result_type, result_value

    def visitFactor(self, ctx):
        if ctx.IntegerLiteral():
            value = int(ctx.IntegerLiteral().getText())
            self.log.append(f"[SEMANTICO] Literal inteiro encontrado: {value}")
            return "Int", value

        if ctx.stringLiteral():
            text = ctx.stringLiteral().getText()
            self.log.append(f"[SEMANTICO] Literal string encontrado: {text}")
            return "String", text

        if ctx.Identifier():
            name = ctx.Identifier().getText()

            self.log.append(f"[SEMANTICO] Uso da variavel '{name}'")

            if name not in self.symbols:
                self.semantic_error(ctx, f"Variavel '{name}' usada sem declaracao previa.")
                return "Unknown", None

            symbol = self.symbols[name]
            return symbol.type, symbol.value

        if ctx.expression():
            return self.visit(ctx.expression())

        return "Unknown", None