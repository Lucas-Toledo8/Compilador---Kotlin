from Antlr.KotlinParserVisitor import KotlinParserVisitor

class Interpretador(KotlinParserVisitor):
        def __init__(self):
            # Memória única para armazenar variáveis de qualquer código
            self.memoria = {}

        # 1. Gerenciamento de Escopo e Decisão (Regra: ifExpression)
        def visitIfExpression(self, ctx):
            condicao = self.visit(ctx.expression())
            if condicao:
                return self.visit(ctx.block(0))
            elif ctx.ELSE():
                # Suporta 'else if' recursivo ou bloco 'else' [Regra: ifExpression ou block(1)]
                if ctx.ifExpression():
                    return self.visit(ctx.ifExpression())
                else:
                    return self.visit(ctx.block(1))
            return None

        # 2. Laços de Repetição (Regra: loopExpression) 
        def visitLoopExpression(self, ctx):
            while self.visit(ctx.expression()):
                self.visit(ctx.block())
            return None

        # 3. Lógica Booleana - Nível OR (Regra: expression) 
        def visitExpression(self, ctx):
            res = self.visit(ctx.logicalAnd(0))
            for i in range(1, len(ctx.logicalAnd())):
                # Se encontrar o token OR (||), aplica a lógica booleana 
                res = res or self.visit(ctx.logicalAnd(i))
            return res

        # 4. Lógica Booleana - Nível AND (Regra: logicalAnd)
        def visitLogicalAnd(self, ctx):
            res = self.visit(ctx.equality(0))
            for i in range(1, len(ctx.equality())):
                # Se encontrar o token AND (&&), aplica a lógica booleana 
                res = res and self.visit(ctx.equality(i))
            return res

        # 5. Igualdade (Regra: equality)
        def visitEquality(self, ctx):
            if ctx.getChildCount() >= 3:
                esq = self.visit(ctx.comparison(0))
                for i in range(1, len(ctx.comparison())):
                    op = ctx.getChild(2*i - 1).getText()
                    dir = self.visit(ctx.comparison(i))
                    if op == '==': esq = (esq == dir)
                    elif op == '!=': esq = (esq != dir)
                return esq
            return self.visit(ctx.comparison(0))

        # 6. Comparações (Regra: comparison)
        def visitComparison(self, ctx):
            if ctx.getChildCount() >= 3:
                esq = self.visit(ctx.arithmetic(0))
                op = ctx.getChild(1).getText()
                dir = self.visit(ctx.arithmetic(1))
                if op == '<': return esq < dir
                if op == '<=': return esq <= dir
                if op == '>': return esq > dir
                if op == '>=': return esq >= dir
            return self.visit(ctx.arithmetic(0))

        # 7. Operações Aritméticas (Regras: arithmetic e term)
        def visitArithmetic(self, ctx):
            res = self.visit(ctx.term(0))
            for i in range(1, len(ctx.term())):
                op = ctx.getChild(2*i - 1).getText()
                val = self.visit(ctx.term(i))
                res = res + val if op == '+' else res - val
            return res

        # 7.1 Operações Aritméticas (Regra: term)
        def visitTerm(self, ctx):
            res = self.visit(ctx.factor(0))
            for i in range(1, len(ctx.factor())):
                op = ctx.getChild(2*i - 1).getText()
                val = self.visit(ctx.factor(i))
                if op == '*': res *= val
                elif op == '/': res //= val if val != 0 else 0
            return res

        # 8. Variáveis e Valores (Regra: factor)
        def visitFactor(self, ctx):
            if ctx.IntegerLiteral(): return int(ctx.IntegerLiteral().getText())
            if ctx.Identifier(): return self.memoria.get(ctx.Identifier().getText(), 0)
            if ctx.stringLiteral(): return self.visit(ctx.stringLiteral())
            if ctx.LPAREN(): return self.visit(ctx.expression())
            return 0

        # 9. Atribuição e Declaração
        def visitAssignment(self, ctx):
            nome = ctx.Identifier().getText()
            self.memoria[nome] = self.visit(ctx.expression())
            return self.memoria[nome]

        def visitDeclaration(self, ctx):
            nome = ctx.Identifier().getText()
            valor = self.visit(ctx.expression()) if ctx.expression() else 0
            self.memoria[nome] = valor
            return valor

        # 10. Chamada de Funções (Regra: functionCall) 
        def visitFunctionCall(self, ctx):
            if ctx.PRINTLN():
                valor = self.visit(ctx.expression())
                if isinstance(valor, str): print(valor)
                else: print(valor, end="  ")
            return None

        def visitStringLiteral(self, ctx):
            return ctx.LineStrText().getText() if ctx.LineStrText() else ""

