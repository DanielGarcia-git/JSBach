grammar jsbach;

root : procDef+ EOF ;

instructions : instruction* ;

instruction : (conditional | while_)
            | (read | write | assign | play | proc | listInstructions)
            ;

listInstructions : listAddElement
                 | listCutElement
                 ;

listAddElement : VAR ADD expr ;

listCutElement : CUT VAR LC expr RC ;

listGetElement : VAR LC expr RC ;

listSize : SIZE VAR ;

conditional : IF expr_bool BEGIN instructions END (ELSE BEGIN instructions END)?;

while_ : WHILE expr_bool BEGIN instructions END ;

read : READ VAR ;

write : WRITE (expr | CADENA)* ;

assign : VAR ASSIGN (expr | list_) ;

play : PLAY list_ #PlayList
     | PLAY (NOTE | VAR) #PlayNoteVar
     ;

list_ : LB (NOTE | NUM)* RB ;

procDef : PROCNAME (VAR)* BEGIN instructions END;
proc : PROCNAME expr* ;

expr_bool : expr (EQ | DIFF | L | G | LEQ | GEQ) expr 
          | NUM
          ;

expr : LP expr RP #Par
     | expr (MULT |  DIV) expr #MultDiv
     | expr MOD expr #Mod
     | expr (SUM | RES)  expr #SumRes
     | (listGetElement | listSize) #ListGetLen
     | NOTE #Note
     | VAR #Var
     | NUM #Num
     ; 

ASSIGN : '<-' ;

READ   : '<?>' ;

WRITE  : '<!>' ;

ADD : '<<' ;

CUT : '8<' ;

SIZE : '#' ;

EQ   : '=' ;
DIFF : '/=';
L    : '<' ;     
G    : '>' ;
LEQ  : '<=';
GEQ  : '>=';

BEGIN : '|:' ;
END   : ':|' ;
LP   : '(' ;
RP   : ')' ;
LB   : '{' ;
RB   : '}' ;
LC   : '[' ;
RC   : ']' ;

IF     : 'if' ;
WHILE  : 'while' ;
ELSE   : 'else' ;

NOTE : ('A' .. 'G')('0' .. '8')* ;

VAR  : [a-z\u0080-\u00FF]([a-zA-Z0-9\u0080-\u00FF] | '_')* ;
PROCNAME  : [A-Z\u0080-\u00FF]([a-zA-Z0-9\u0080-\u00FF] | '_')* ;
NUM  : [0-9]+ ;
PLAY   : '<:>' ;

MULT : '*' ;
DIV  : '/' ;
SUM  : '+' ;
RES  : '-' ;
MOD  : '%' ;

CADENA : '"' (~('"' | '\n' | '\r' | '\t'))* '"';
WS  :   [ \n]+ -> skip ;
NL :(('\r' | '\n')) ;
COMMENT : '~~~' (('~~~' NL) | ('~~~' ~('\n'|'\r')) | NL | ~( '\n' | '\r'))* '~~~' -> skip;
