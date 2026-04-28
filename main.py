import glob
import sys
import os
from antlr4 import *
from antlr4.tree.Trees import Trees

from interpretador import Interpretador
from interpretadorSematica import InterpretadorSematica


# Ajuste do caminho para a pasta Antlr
sys.path.append(os.path.join(os.path.dirname(__file__), 'Antlr'))

from Antlr.KotlinLexer import KotlinLexer
from Antlr.KotlinParser import KotlinParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: Símbolo '{offendingSymbol.text}' inesperado.")

class MyLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo inválido.")

def generate_dot(node, parser, file):
    """Gera o formato DOT recursivamente para o Graphviz"""
    text = Trees.getNodeText(node, parser.ruleNames).replace('"', '\\"')
    file.write(f'  n{id(node)} [label="{text}"];\n')
    for i in range(node.getChildCount()):
        child = node.getChild(i)
        file.write(f'  n{id(node)} -> n{id(child)};\n')
        generate_dot(child, parser, file)


def main():
    
    
    # 1. Busca todos os arquivos que terminam com .kt na pasta atual
    arquivos_kt = glob.glob("Casos_de_Teste/*.kt")

    if not arquivos_kt:
        print("\nNenhum arquivo .kt encontrado na pasta!\n")
        return

    print("\n--- Arquivos encontrados ---")
    for i, nome in enumerate(arquivos_kt):
        arquivo_nome = os.path.basename(nome)
        print(f"[{i}] {arquivo_nome}")

    try:
        escolha = int(input("\nEscolha o número do arquivo para rodar (ou aperte Enter para o primeiro): ") or 0)
        arquivo_nome = arquivos_kt[escolha]
    except (ValueError, IndexError):
        print("Seleção inválida. Saindo...")
        return

    print(f"\nProcessando: {os.path.basename(arquivo_nome)}")
    

    input_stream = FileStream(arquivo_nome, encoding='utf-8')
    
    # 1. Lexer
    lexer = KotlinLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyLexerErrorListener())

    # 2. Tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill() 
    
    print("\n--- LOG DE TOKENS ---\n")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            tipo = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"
            print(f"<{tipo}, {token.text}, {token.line}, {token.column}>")

    # 3. Parser
    token_stream.reset() # Volta para o início para o Parser ler
    parser = KotlinParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    
   
    tree = parser.kotlinFile() 
    
    if parser.getNumberOfSyntaxErrors() == 0:
        print("\n--- INICIANDO PERCURSO DE EXECUÇÃO (LOG SEMÂNTICO) ---\n")
        
        executor = InterpretadorSematica() # Esta é a classe importada do seu interpretadorSematica.py
        executor.visit(tree)       # Aqui ele percorre a árvore e imprime os logs
       
    if parser.getNumberOfSyntaxErrors() == 0:
        
        print("\n--- EXECUÇÃO (Interpretador Terminal) ---\n")
        
        executor = Interpretador() # Esta é a classe importada do seu interpretador.py
        executor.visit(tree)       # Aqui ele percorre a árvore e imprime os logs
        
        print("\n-----------------------------\n")
    
    
    if parser.getNumberOfSyntaxErrors() == 0:
        print("Análise sintática finalizada com sucesso! Código válido.")
        
        while True:
            try:
                opcao = input(f"\nGerar arquivo DOT para '{os.path.basename(arquivo_nome)}'? [S] sim / [Qualquer tecla] sair: ").strip().upper()
                
                if opcao == "S":
                    # Usando f-string para o nome do arquivo .dot
                    nome_dot = f"{arquivo_nome}.dot"
                    with open(nome_dot, "w", encoding="utf-8") as f:
                        f.write("digraph AST {\n")
                        f.write('  fontname="Arial";\n')
                        f.write(f'  label="AST: {os.path.basename(arquivo_nome)}";\n')
                        f.write('  labelloc="t";\n') 
                        f.write('  node [fontname="Arial", shape=ellipse];\n')
                        
                        generate_dot(tree, parser, f)
                        f.write("}\n")
                    print(f"\nArquivo '{os.path.basename(nome_dot)}' gerado com sucesso!")
                else:
                    print("\nEncerrando sem gerar o gráfico...")
                break 
            except EOFError:
                break 
    else:
        print(f"Análise finalizada com {parser.getNumberOfSyntaxErrors()} erro(s).") 
      
        
if __name__ == '__main__':
    main()