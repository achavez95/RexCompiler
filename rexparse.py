#An implementation of Rex

from ply import *
import rexlex
import cubo

tokens = rexlex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'POWER')
)

#A Rex program is a series of statements.

def p_program(p) :
    '''program : PROGRAM ID SEMI function
    | PROGRAM ID SEMI var function'''
    print (p[0])

def p_function(p) :
    '''function : FUNCTION ID LPAREN parameter RPAREN RETURN type block
    | FUNCTION ID LPAREN RPAREN RETURN type block
    | FUNCTION ID LPAREN RPAREN block
    | FUNCTION ID LPAREN parameter RPAREN block'''
    print (p[0])

def p_parameter(p) :
    '''parameter : ID COLON type'''
    print (p[0])

def p_block(p) :
    '''block : LBRACE statement RBRACE'''
    print (p[0])

def p_statement(p) :
    '''statement : condition
    | assignment SEMI
    | while
    | for
    | comment
    | print SEMI
    | var SEMI'''
    print (p[0])

def p_print(p) :
    '''print : PRINT LPAREN expression RPAREN
    | PRINT LPAREN STRING_CONS RPAREN
    | PRINT LPAREN ID RPAREN'''

def p_comment(p) :
    '''comment : COMMENT ID'''
    print (p[0])

def p_for(p) :
    '''for : LPAREN assignment expression SEMI expression RPAREN block'''
    print (p[0])

def p_while(p) :
    '''while : WHILE LPAREN expression RPAREN block'''
    print (p[0])

def p_condition(p) :
    '''condition : LPAREN expression RPAREN block ELSE block
    | LPAREN expression RPAREN block'''
    print (p[0])

def p_var(p) :
    '''var : VAR var1 COLON type'''
    print (p[0])

def p_var1(p) :
    '''var1 : ID
    | ID COMMA var1'''
    print (p[0])

def p_type(p) :
    '''type : BOOLEAN
    | INTEGER
    | DECIMAL
    | STRING
    | FRACTION'''
    print (p[0])

def p_assignment(p) :
    '''assignment : ID EQUALS expression'''
    print (p[0])

def p_expression(p) :
    '''expression : expression OR express
    | express'''
    print (p[0])

def p_express(p) :
    '''express : express AND expr
    | expr'''
    print (p[0])

def p_expr(p) :
    '''expr : NOT exp
    | exp'''
    print (p[0])

def p_exp(p) :
    '''exp : exp EQUALS EQUALS ex
    | exp DIF ex
    | exp GE ex
    | exp LE ex
    | exp NE ex
    | exp GT ex
    | exp LT ex
    | ex'''
    print (p[0])

def p_ex(p) :
    '''ex : ex PLUS term
    | ex MINUS term
    | term'''
    print (p[0])

def p_term(p) :
    '''term : term MODULO factor
    | term DIVIDE factor
    | term TIMES factor
    | factor '''
    print (p[0])

def p_factor(p) :
    '''factor : factor POWER unit
    | unit '''
    print (p[0])

def p_unit(p) :
    '''unit : ID LBRACK INTEGER_CONS RBRACK LBRACK INTEGER_CONS RBRACK
    | ID LBRACK INTEGER_CONS RBRACK
    | ID'''
    print (p[0])

def p_error(p) :
    if p:
        print ("Syntax error at '%s'" % p.value)
    else:
        print ("Syntax error at EOF")


yacc.yacc()

data = 'program'
t = yacc.parse(data)
print (t)
