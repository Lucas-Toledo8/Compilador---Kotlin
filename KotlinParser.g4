parser grammar KotlinParser;

options {
    tokenVocab = KotlinLexer;
}

// Regra inicial
kotlinFile : (functionDefinition | statement)* EOF ;

functionDefinition : FUN Identifier LPAREN RPAREN block ;

statement : declaration 
        | assignment
        | loopExpression 
        | ifExpression 
        | functionCall 
        | block ;

stringLiteral : QUOTE_OPEN LineStrText? QUOTE_CLOSE ;

declaration : VAR Identifier (COLON type)? (ASSIGNMENT expression)? SEMICOLON ;
type        : INT_TYPE | STR_TYPE ;

assignment  : Identifier ASSIGNMENT expression SEMICOLON ;


ifExpression    : IF LPAREN expression RPAREN block (ELSE (block | ifExpression))? ;

loopExpression  : WHILE LPAREN expression RPAREN block ;
block           : LCURL (statement)* RCURL ;

functionCall : PRINTLN LPAREN expression RPAREN SEMICOLON
             | Identifier ASSIGNMENT READLN LPAREN RPAREN SEMICOLON ;

// --- HIERARQUIA DE EXPRESSÕES (LÓGICA BOOLEANA) ---

// 1. Nível mais baixo: OR (ex: A || B)
expression : logicalAnd (OR logicalAnd)* ;

// 2. Nível médio: AND (ex: A && B)
logicalAnd : equality (AND equality)* ;

// 3. Igualdade e Diferença (ex: ==, !=)
equality : comparison ((EQEQ | EXCL_EQ) comparison)* ;

// 4. Comparações de Grandeza (ex: <, >, <=, >=)
comparison : arithmetic ((LE | GE | LANGLE | RANGLE) arithmetic)* ;

// 5. Aritmética (Soma e Subtração)
arithmetic : term ((ADD | SUB) term)* ;

// 6. Termos (Multiplicação e Divisão)
term : factor ((MULT | DIV) factor)* ;

// 7. Base da Pirâmide
factor : LPAREN expression RPAREN | Identifier | IntegerLiteral | stringLiteral ;