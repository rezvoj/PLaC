grammar Grammar;


// Lexer rules
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;

INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
READ: 'read';
WRITE: 'write';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';

BOOL_LIT: 'true' | 'false';
STRING_LIT: '"' ~["]* '"';
FLOAT_LIT: [0-9]+ '.' [0-9]+;
INT_LIT: [0-9]+;
ID: [a-zA-Z] [a-zA-Z0-9_]*;


// Parser rules
program: statement* EOF;

statement:
    ';'
    | type (ID ',')* ID ';'
    | expression ';'
    | READ (ID ',')* ID ';'
    | WRITE (expression ',')* expression ';'
    | '{' statement* '}'
    | IF '(' expression ')' statement ( ELSE statement )?
    | WHILE '(' expression ')' statement
    | FOR '(' (expression)? ';' expression ';' (expression)? ')' statement
    ;

type: INT | FLOAT | BOOL | STRING;

expression:
    primary
    | uop='-' expression
    | uop='!' expression
    | expression bop=('*' | '/' | '%') expression
    | expression bop=('+' | '-' | '.') expression
    | expression bop=('<' | '>') expression
    | expression bop=('==' | '!=') expression
    | expression bop='&&' expression
    | expression bop='||' expression
    | <assoc = right> expression bop='=' expression
    ;

primary: '(' expression ')' | INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | ID;
