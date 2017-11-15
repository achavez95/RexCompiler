# -*- coding: utf-8 -*- 

#An implementation of Rex

from ply import *
import rexlex
from cubo import *
from stack import *
from cuadruplo import *
from variable import *

tokens = rexlex.tokens

class Memoria:
    def __init__(self):
        self.memoria = {}

    def guardaTemporal(valor):
        count = 10000
        
    

#Variables globales
intglob = {}
intglob_count = 0
decglob = {}
decglob_count = 100
fracglob = {}
fracglob_count = 200
strglob = {}
strglob_count = 300
boolglob = {}
boolglob_count = 400

#Variables locales
intloc = {}
intloc_count = 500
decloc = {}
decloc_count = 700
fracloc = {}
fracloc_count = 900
strloc = {}
strloc_count = 1100
boolloc = {}
boolloc_count = 1300

#Temporales

inttemp = {}
inttemp_count = 1500
dectemp = {}
dectemp_count = 1800
fractemp = {}
fractemp_count = 2100
strtemp = {}
strtemp_count = 2400
booltemp = {}
booltemp_count = 2700

templist = []
temp_count = 1500

#Constantes
intconst = []
intconst_count = 3000
decconst = []
decconst_count = 3300
fracconst = []
fracconst_count = 3600
strconst = []
strconst_count = 3900
boolconst = []
boolconst_count = 4100

#Lista de cuadruplos y pilas
cuadruplos = []
cuadcount = 0
pilao = Stack()
ptipos = Stack()
psaltos = Stack()
piladim = []

#Lista de variables
listavar = []

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'GT', 'LT', 'GE', 'LE', 'NE', 'SAME'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'POWER')
)

#A Rex program is a serie of statements.
def p_program(p):
    '''program : PROGRAM ID SEMI function
    | PROGRAM ID SEMI var function'''
    print (p[0])

def p_function(p):
    '''function : FUNCTION ID LPAREN parameter RPAREN RETURN type block
    | FUNCTION ID LPAREN RPAREN RETURN type block
    | FUNCTION ID LPAREN RPAREN block
    | FUNCTION ID LPAREN parameter RPAREN block'''
    print (p[0])

def p_parameter(p):
    '''parameter : ID COLON type
    | ID COLON type COMMA parameter'''
    print (p[0])

def p_block(p):
    '''block : LBRACE statements RBRACE
    | LBRACE RBRACE'''
    print (p[0])

def p_statements(p):
    '''statements : statement
    | statement statements
    '''

def p_statement(p):
    '''statement : condition
    | assignment 
    | while
    | for
    | comment
    | print
    | var'''
    print (p[0])

def p_print(p):
    '''print : PRINT LPAREN expression RPAREN SEMI
    | PRINT LPAREN STRING_CONS RPAREN SEMI
    | PRINT LPAREN ID RPAREN SEMI'''

def p_comment(p):
    '''comment : COMMENT ID'''
    print (p[0])

def p_for(p):
    '''for : LPAREN assignment expression SEMI expression RPAREN block'''
    print (p[0])

def p_while(p):
    '''while : WHILE LPAREN expression RPAREN block'''
    print (p[0])

def p_condition(p):
    '''condition : IF LPAREN expression RPAREN block ELSE block
    | IF LPAREN expression RPAREN block'''
    print (p[0])

def p_var(p):
    '''var : VAR type var1 SEMI'''
    print (p[0])

def p_var1(p):
    '''var1 : ID savevar
    | ID savevar COMMA var1'''
    print (p[0])

def p_settypeint(p):
    '''settypeint : empty'''
    global type
    type = 0

def p_settypedec(p):
    '''settypedec : empty'''
    global type
    type = 1

def p_settypefrac(p):
    '''settypefrac : empty'''
    global type
    type = 2

def p_settypestring(p):
    '''settypestring : empty'''
    global type
    type = 3

def p_settypebool(p):
    '''settypebool : empty'''
    global type
    type = 4

def p_savevar(p):
    '''savevar : empty'''
    global var
    print (p[-1])
    var = Variable(type, p[-1], None, None)
    listavar.append(var)

def p_type(p):
    '''type : BOOLEAN settypebool
    | INTEGER settypeint
    | DECIMAL settypedec
    | STRING settypestring
    | FRACTION settypefrac'''
    print (p[0])

def p_assignment(p):
    '''assignment : type ID EQUALS expression SEMI
    | ID EQUALS expression SEMI'''
    print (p[0])

def p_expression(p):
    '''expression : exp
    '''
    print (p[0])

def p_exp(p):
    '''exp : exp OR exp
    | exp AND exp
    | exp SAME exp
    | exp DIF exp
    | exp GE exp
    | exp LE exp
    | exp NE exp
    | exp GT exp
    | exp LT exp
    | exp PLUS exp
    | exp MINUS exp
    | exp MODULO exp
    | exp DIVIDE exp
    | exp TIMES exp
    | exp POWER exp'''
    
    a = pilao.pop()
    tipoa = ptipos.pop()
    b = pilao.pop()
    tipob = ptipos.pop()
    if (tipoResultante(tipob, tipoa, getNumOp(p[2])) != -1):
        cuadruplo = Cuadruplo(getNumOp(p[2]), b, a, 1000)
        cuadruplos.append(cuadruplo)
        global cuadcount
        cuadcount += 1
        pilao.push(1000)
        ptipos.push(tipoResultante(tipob, tipoa, getNumOp(p[2])))
    else:
        print ("Syntax error at '%s', incompatible types" % p[2])
        
def p_exp2(p):
    '''exp : ID pushid
    | ID LBRACK expression RBRACK pushid
    | LBRACK exp RBRACK
    | INTEGER_CONS settypeint pushcons
    | STRING_CONS settypestring pushcons 
    | FRACTION_CONS settypefrac pushcons 
    | DECIMAL_CONS settypedec pushcons 
    | TRUE settypebool pushcons
    | FALSE settypebool pushcons'''
    print (p[0])

def p_expunary(p):
    '''exp : NOT exp'''

    a = pilao.pop()
    tipoa = ptipos.pop()
    if (tipoa == 4):
        cuadruplo = Cuadruplo(14, a, None, 1000)
        cuadruplos.append(cuadruplo)
        cuadcount
        cuadcount += 1
        pilao.push(1000)
        ptipos.push(4)

def p_expgroup(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]

def p_pushtype(p):
    '''pushtype : empty'''
    global type
    tipo = [x.type for x in listavar if x.id == p[-1]]
    if tipo:
        type = tipo[0]
    ptipos.push(type)
    print(type)

def p_pushid(p):
    '''pushid : pushtype'''
    pilao.push(p[-1])

def p_pushcons(p):
    '''pushcons : pushtype'''
    pilao.push(p[-2])
    print(p[-2])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print ("Syntax error at '%s'" % p.value)
    else:
        print ("Syntax error at EOF")


yacc.yacc()

# data = 'program a; function b () { var x : int; } '
data = 'program a; function b (x : int, y : int) { var int x,y; x=2+3;} '

t = yacc.parse(data)
print (t)
print (pilao)
print (ptipos)
for x in range (0, len(cuadruplos)) :
    print (cuadruplos[x].pos1, ',' , cuadruplos[x].pos2, ',' ,cuadruplos[x].pos3, ',', cuadruplos[x].pos4)
