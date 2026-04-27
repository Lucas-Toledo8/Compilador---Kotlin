lexer grammar KotlinLexer;


// --- PALAVRAS RESERVADAS ---
FUN      : 'fun' ;
VAR      : 'var' ;
IF       : 'if' ;
ELSE     : 'else' ;
WHILE    : 'while' ;
PRINTLN  : 'println' ; 
READLN   : 'readln' ;
INT_TYPE : 'Int' ;
STR_TYPE : 'String' ;

// --- SIMBOLOS E PONTUACAO ---
ASSIGNMENT : '=' ;
COLON      : ':' ;
SEMICOLON  : ';' ;
LPAREN     : '(' ;
RPAREN     : ')' ;
LCURL      : '{' ;
RCURL      : '}' ;


// --- OPERADORES LÓGICOS ---
AND      : '&&' ;
OR       : '||' ;

// --- OPERADORES DE COMPARAÇÃO ---
LE       : '<=' ;
GE       : '>=' ;
EXCL_EQ  : '!=' ;
EQEQ     : '==' ;
LANGLE   : '<' ;
RANGLE   : '>' ;

// --- OPERADORES ARITMÉTICOS ---
ADD      : '+' ;
SUB      : '-' ;
MULT     : '*' ;
DIV      : '/' ;


// --- LOGICA DE STRING COM MODOS ---
QUOTE_OPEN : '"' -> pushMode(LineString) ;

// --- REGRAS GERAIS ---
Identifier     : [a-zA-Z_] [a-zA-Z0-9_]* ;
IntegerLiteral : [0-9]+ ;
WS             : [ \t\r\n]+ -> skip ;
LineComment    : '//' ~[\r\n]* -> skip ;

// --- MODO DE STRING ---
mode LineString;
LineStrText    : ~["\r\n]+ ;
QUOTE_CLOSE    : '"' -> popMode ;