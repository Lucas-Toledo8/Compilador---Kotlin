# Trabalho de Compilador: Kotlin

Este projeto consiste em um **Front-end de Compilador** para uma versão simplificada da linguagem Kotlin, desenvolvido com **ANTLR4** e **Python**. O sistema realiza a análise léxica (com log de tokens) e a análise sintática, gerando uma **AST (Abstract Syntax Tree)** em formato Graphviz (.dot).

## Estrutura do Projeto

* `Antlr/`: Pasta contendo os arquivos gerados (Lexer, Parser, Tokens).
* `KotlinLexer.g4`: Gramática léxica (Scanner).
* `KotlinParser.g4`: Gramática sintática (Parser).
* `main.py`: Script principal de execução e geração da AST.
* `/Casos_deTeste`: Arquivos de teste com o algoritmo e os AST `.dot`.
* `antlr-4.13.2-complete.jar`: Binário do ANTLR necessário para compilação.

---

### 1. Pré-requisitos

* **Java Runtime Environment (JRE)** instalado e configurado no PATH.
* **Python 3.x** instalado.
* Biblioteca do ANTLR para Python:

    ```bash
    pip install antlr4-python3-runtime==4.13.2
    ```

    ou

    ```bash
    pip install -r requirements.txt
    ```

### 2. Gerar o Compilador (Lexer e Parser)

Sempre que alterar os arquivos `.g4`, rode os seguintes comandos no terminal:

 **Passo A: Gerar o Lexer.**  

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -o Antlr KotlinLexer.g4
```

 **Passo B: Gerar o Parser.**

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o Antlr -lib Antlr KotlinParser.g4
```

> **Nota:** Após gerar, certifique-se de que o arquivo `Antlr/KotlinLexer.tokens` exista, pois o Parser depende dele para funcionar.

### 3. Executar a Análise

Para processar o arquivo `pascal.kt` e gerar o log de tokens e a árvore sintática:

```bash
python main.py
```

---

## Visualização da AST (Árvore Sintática)

Após a execução bem-sucedida, um arquivo chamado `tree.dot` será gerado na raiz do projeto.  

**Para visualizar o gráfico:**

1. Copie o conteúdo de `tree.dot`.

2. Cole no site [Graphviz Online](https://dreampuf.github.io/GraphvizOnline/).

3. O gráfico mostrará a estrutura hierárquica do código Kotlin processado.

---

## Funcionalidades Implementadas

* **Modos Léxicos:** Tratamento de Strings complexas usando `pushMode` e `popMode`.
* **Estruturas Suportadas:** Funções (`fun main`), loops (`while`), condicionais (`if, else if, else`), declarações de variáveis e expressões aritméticas.
* **Tratamento de Erros:** Listeners customizados para identificar linha e coluna de erros léxicos e sintáticos.
