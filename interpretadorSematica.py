from Antlr.KotlinParserVisitor import KotlinParserVisitor

class InterpretadorSematica(KotlinParserVisitor):
        def __init__(self):
            # Memória única para armazenar variáveis de qualquer código
            self.memoria = {}

        # 1. Gerenciamento de Escopo e Decisão (Regra: ifExpression)
        def visitIfExpression(self, ctx):
            
            condicao = self.visit(ctx.expression())
            print(f"[FLUXO] Avaliando IF: Condição resultante é {condicao}")
            
            if condicao:
                print("[FLUXO] -> Executando bloco verdadeiro (IF)")
                return self.visit(ctx.block(0))
            elif ctx.ELSE():
                print("[FLUXO] -> Condição Falsa. Seguindo para o ELSE")
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
                val_segundo = self.visit(ctx.equality(i))
                antigo_res = res
                res = res and val_segundo
                print(f"[LÓGICA] Operação AND: ({antigo_res} && {val_segundo}) -> {res}")
            return res

        # 5. Comparações de Igualdade (Regra: equality)
        def visitEquality(self, ctx):
            if ctx.getChildCount() >= 3:
                esq = self.visit(ctx.comparison(0))
                op = ctx.getChild(1).getText()
                dir = self.visit(ctx.comparison(1))
                res = (esq == dir) if op == '==' else (esq != dir)
                print(f"[SEMÂNTICO] Verificando igualdade: {esq} {op} {dir} -> {res}") # Log de comparação de igualdade
                return res
            return self.visit(ctx.comparison(0))

        # 6. Comparações de Grandeza (Regra: comparison)
        def visitComparison(self, ctx):
            if ctx.getChildCount() >= 3:
                esq = self.visit(ctx.arithmetic(0))
                op = ctx.getChild(1).getText()
                dir = self.visit(ctx.arithmetic(1))
                # Log de comparação de grandeza
                res = None
                if op == '<': res = esq < dir
                elif op == '<=': res = esq <= dir
                elif op == '>': res = esq > dir
                elif op == '>=': res = esq >= dir
                print(f"[SEMÂNTICO] Comparando grandeza: {esq} {op} {dir} -> {res}")
                return res
            return self.visit(ctx.arithmetic(0))

        # 7. Operações Aritméticas (Regras: arithmetic e term)
        def visitArithmetic(self, ctx):
            res = self.visit(ctx.term(0))
            for i in range(1, len(ctx.term())):
                op = ctx.getChild(2*i - 1).getText()
                val = self.visit(ctx.term(i))
                res = res + val if op == '+' else res - val
            return res

        # 7.1 Operações Aritméticas (Regras: arithmetic e term)
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
            valor = self.visit(ctx.expression())
            self.memoria[nome] = valor
            print(f"[MEMÓRIA] Atualizando '{nome}' para: {valor}") # Log de atribuição
            return valor
        
        def visitDeclaration(self, ctx):
            nome = ctx.Identifier().getText()
            valor = self.visit(ctx.expression()) if ctx.expression() else 0
            self.memoria[nome] = valor
            print(f"[MEMÓRIA] Alocando '{nome}' com valor inicial: {valor}") # Log de memória
            return valor

        # 10. Chamada de Funções (Regra: functionCall)  
        def visitFunctionCall(self, ctx):
            if ctx.PRINTLN():
                valor = self.visit(ctx.expression())
                print(f"[SAÍDA] println: {valor}") # Log universal de saída
            return None
        
        def visitStringLiteral(self, ctx):
            texto = ctx.LineStrText().getText() if ctx.LineStrText() else ""
            print(f"[DADO] Lendo texto: \"{texto}\"") # Log de processamento de string
            return texto





