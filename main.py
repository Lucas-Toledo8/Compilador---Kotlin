# main.py
# Pipeline: analise lexica + sintatica + semantica + geracao de codigo JavaScript

import glob
import os
import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

sys.path.append(os.path.join(os.path.dirname(__file__), "Antlr"))

from Antlr.KotlinLexer import KotlinLexer
from Antlr.KotlinParser import KotlinParser

from semantic_analyzer import SemanticAnalyzer
from gerador_js import JavaScriptGenerator


class CompilerErrorListener(ErrorListener):
    def __init__(self, fase):
        super().__init__()
        self.fase = fase
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(
            f"[ERRO {self.fase.upper()}] linha {line}, coluna {column} - {msg}"
        )


def generate_dot(node, parser, file):
    """Gera o formato DOT recursivamente para o Graphviz."""
    text = Trees.getNodeText(node, parser.ruleNames).replace('"', '\\"')
    file.write(f'  n{id(node)} [label="{text}"];\n')

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        file.write(f'  n{id(node)} -> n{id(child)};\n')
        generate_dot(child, parser, file)


def imprimir_tokens(token_stream, lexer):
    print("\n--- LOG DE TOKENS ---")

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            tipo = (
                lexer.symbolicNames[token.type]
                if token.type < len(lexer.symbolicNames)
                else "UNKNOWN"
            )

            print(f"<{tipo}, {token.text}, {token.line}, {token.column}>")


def main():
    
    

    # 1. Definimos o caminho das pastas como strings simples
    pastaA = "Casos_de_Teste/*.kt"
    pastaB = "Casos_de_Teste_2/*.kt"

    # 2. Lemos a entrada do usuário e padronizamos para maiúscula com .upper()
    opcaoPasta = input("\nQual pasta de teste utilizar [A] ou [B]: ").upper()

    # 3. Comparamos diretamente o valor digitado pelo usuário
    if opcaoPasta == "A":
        arquivos_kt = glob.glob(pastaA)
      

    elif opcaoPasta == "B":
        arquivos_kt = glob.glob(pastaB)
        

    else:
        arquivos_kt = []
        print("Opção inválida! Nenhuma pasta selecionada.")

        
    
  

    if not arquivos_kt:
        print("Nenhum arquivo .kt encontrado na pasta!")
        return

    print("\n--- Arquivos encontrados ---")

    for i, nome in enumerate(arquivos_kt):
        arquivo_nome = os.path.basename(nome)
        print(f"[{i}] {arquivo_nome}")

    try:
        escolha = int(
            input("\nEscolha o numero do arquivo para rodar (ou Enter para o primeiro): ")
            or 0
        )
        arquivo_nome = arquivos_kt[escolha]

    except (ValueError, IndexError):
        print("Selecao invalida. Saindo...")
        return

    print(f"\nProcessando: {os.path.basename(arquivo_nome)}")

    # =========================
    # ANALISE LEXICA
    # =========================

    input_stream = FileStream(arquivo_nome, encoding="utf-8")

    lexer = KotlinLexer(input_stream)
    lexical_listener = CompilerErrorListener("lexico")

    lexer.removeErrorListeners()
    lexer.addErrorListener(lexical_listener)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    imprimir_tokens(token_stream, lexer)

    # =========================
    # ANALISE SINTATICA
    # =========================

    token_stream.reset()

    parser = KotlinParser(token_stream)
    syntax_listener = CompilerErrorListener("sintatico")

    parser.removeErrorListeners()
    parser.addErrorListener(syntax_listener)

    print("\n--- INICIANDO ANALISE SINTATICA ---")

    tree = parser.kotlinFile()

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Analise sintatica finalizada com sucesso! Codigo valido.")
    else:
        print(f"Analise sintatica finalizada com {parser.getNumberOfSyntaxErrors()} erro(s).")

    # =========================
    # GERACAO DO DOT
    # =========================

    if parser.getNumberOfSyntaxErrors() == 0:
        opcao_dot = input(
            f"\nGerar arquivo DOT para '{os.path.basename(arquivo_nome)}'? [S] sim / [Qualquer tecla] nao: "
        ).strip().upper()

        if opcao_dot == "S":
            nome_dot = f"{arquivo_nome}.dot"

            with open(nome_dot, "w", encoding="utf-8") as f:
                f.write("digraph AST {\n")
                f.write('  fontname="Arial";\n')
                f.write(f'  label="AST: {os.path.basename(arquivo_nome)}";\n')
                f.write('  labelloc="t";\n')
                f.write('  node [fontname="Arial", shape=ellipse];\n')

                generate_dot(tree, parser, f)

                f.write("}\n")

            print(f"Arquivo '{os.path.basename(nome_dot)}' gerado com sucesso!")

    # =========================
    # ERROS LEXICOS/SINTATICOS
    # =========================

    if lexical_listener.errors:
        print("\n===== ERROS LEXICOS =====")
        for error in lexical_listener.errors:
            print(error)

    if syntax_listener.errors:
        print("\n===== ERROS SINTATICOS =====")
        for error in syntax_listener.errors:
            print(error)

    if lexical_listener.errors or syntax_listener.errors:
        print("\nAnalise semantica e geracao de codigo nao executadas por causa de erros anteriores.")
        return

    # =========================
    # ANALISE SEMANTICA
    # =========================

    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)

    logs = getattr(analyzer, "log", getattr(analyzer, "logs", []))

    print("\n===== LOG SEMANTICO =====")

    for item in logs:
        print(item)

    if analyzer.errors:
        print("\n===== ERROS SEMANTICOS =====")
        for error in analyzer.errors:
            print(error)

        print("\nGeracao de codigo nao executada por causa de erros semanticos.")
        return

    print("\nAnalise semantica concluida sem erros.")

    # =========================
    # GERACAO DE CODIGO JS
    # =========================

    opcao_js = input(
        f"\nGerar JavaScript para '{os.path.basename(arquivo_nome)}'? [S] sim / [Qualquer tecla] nao: "
    ).strip().upper()

    if opcao_js == "S":
        generator = JavaScriptGenerator(symbols=analyzer.symbols)
        js_code = generator.visit(tree)

        nome_js = os.path.splitext(arquivo_nome)[0] + ".js"

        with open(nome_js, "w", encoding="utf-8") as f:
            f.write(js_code)

        print(f"Arquivo JavaScript gerado com sucesso: {nome_js}")

    print("\n===== COMPILACAO FINALIZADA =====")


if __name__ == "__main__":
    main()
