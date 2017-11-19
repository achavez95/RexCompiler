# -*- coding: utf-8 -*- 

#An implementation of Rex

from ply import *
import rexlex
from cubo import *
from stack import *
from cuadruplo import *
from variable import *
import sys

tokens = rexlex.tokens

class Memoria:
    def __init__(self):
        self.memoria = {}

    def printVars(self):
        print("MEMORIA", listavar, self.memoria.items())

    def allocate(self, tipo, context, size):
        offset = 0 + 5000*context
        
        if tipo == 0:
            count = 0 + offset
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None:
                    break
                count+=1
            for i in range(count, count+size):
                self.memoria[i] = "NI"
            return count

        if tipo == 1:
            count = 1000 + offset
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None:
                    break
                count+=1
            for i in range(count, count+size):
                self.memoria[i] = "NI"
            return count

        if tipo == 2:
            count = 2000 + offset
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None:
                    break
                count+=1
            for i in range(count, count+size):
                self.memoria[i] = "NI"
            return count

        if tipo == 3:
            count = 3000 + offset
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None:
                    break
                count+=1
            for i in range(count, count+size):
                self.memoria[i] = "NI"
            return count

        if tipo == 4:
            count = 4000 + offset
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None:
                    break
                count+=1
            for i in range(count, count+size):
                self.memoria[i] = "NI"
            return count

    def allocateCons(self, tipo, valor):
        if tipo == 0:
            count = 200000
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None or self.memoria[count] == valor:
                    break
                count+=1
            self.memoria[count] = valor
            return count

        if tipo == 1:
            count = 210000
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None or self.memoria[count] == valor:
                    break
                count+=1
            self.memoria[count] = valor
            return count

        if tipo == 2:
            count = 220000
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None or self.memoria[count] == valor:
                    break
                count+=1
            self.memoria[count] = valor
            return count

        if tipo == 3:
            count = 230000
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None or self.memoria[count] == valor:
                    break
                count+=1
            self.memoria[count] = valor
            return count

        if tipo == 4:
            count = 240000
            for i in self.memoria.items():
                if not count in self.memoria:
                    break
                elif self.memoria[count] == None or self.memoria[count] == valor:
                    break
                count+=1
            self.memoria[count] = valor
            return count

    def updateVar(self, id, value):
        self.memoria[id] = value

    def deleteVar(self, id):
        del self.memoria[id]

memoria = Memoria()

context = 0

#Lista de cuadruplos y pilas
cuadruplos = []
pilao = Stack()
ptipos = Stack()
psaltos = Stack()
piladim = []

#Lista de variables
listavar = []

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'EXMARK'),
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
    | dowhile
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

def p_dowhile(p) :
    '''dowhile : DO pushjump block WHILE LPAREN expression RPAREN gotot'''
    print (p[0])

def p_pushjump(p) :
    '''pushjump : empty'''
    psaltos.push(len(cuadruplos)+1)

def p_gotot(p) :
    '''gotot : empty'''
    a = pilao.pop()
    tipoa = ptipos.pop()
    if (tipoa == 4) :
        jump = psaltos.pop()
        cuadruplo = Cuadruplo(16, a, None, jump)
        cuadruplos.append(cuadruplo)
        psaltos.push(len(cuadruplos) - 1)
    else:
        print ("Syntax error at '%s', incompatible types" % p[-1]) 

def p_while(p):
    '''while : WHILE pushjump LPAREN expression RPAREN gotof block gotowhile'''
    print (p[0])

def p_gotowhile(p):
    '''gotowhile : empty'''
    index = psaltos.pop()
    jump = psaltos.pop()
    cuadruplo = Cuadruplo(15, None, None, jump)
    cuadruplos.append(cuadruplo)
    cuadruplos[index].updatedir(len(cuadruplos) + 1)

def p_condition(p):
    '''condition : IF LPAREN expression RPAREN gotof block ELSE gotoif block updatejump
    | IF LPAREN expression RPAREN gotof block updatejump'''
    print (p[0])
    
#Generación de cuadruplo goto para IF
def p_gotoif(p):
    '''gotoif : empty'''
    cuadruplo = Cuadruplo(15, None, None, None)
    cuadruplos.append(cuadruplo)
    index = psaltos.pop()
    cuadruplos[index].updatedir(len(cuadruplos) + 1)
    psaltos.push(len(cuadruplos) - 1)

def p_gotof(p):
    '''gotof : empty'''
    a = pilao.pop()
    tipoa = ptipos.pop()
    if (tipoa == 4) :
        cuadruplo = Cuadruplo(17, a, None, None)
        cuadruplos.append(cuadruplo)
        psaltos.push(len(cuadruplos) - 1)
    else:
        print ("Syntax error at '%s', incompatible types" % p[-1])

def p_updatejump(p):
    '''updatejump : empty'''
    index = psaltos.pop()
    cuadruplos[index].updatedir(len(cuadruplos) + 1)

def p_var(p):
    '''var : VAR type var1 SEMI'''
    print (p[0])

def p_var1(p):
    '''var1 : ID pushid savevar allocatevar
    | ID pushid savevar allocatevar COMMA var1
    | ID pushid savevar LBRACK INTEGER_CONS updatesize RBRACK allocatevar COMMA var1
    | ID pushid savevar LBRACK INTEGER_CONS updatesize RBRACK allocatevar'''
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
    id = pilao.pop()
    tipo = ptipos.pop()
    tipo = type
    for v in listavar:
        if v.id == id:
            listavar.remove(v)
            memoria.deleteVar(v.memory)
    print("ID: ", id)
    var = Variable(tipo, id, None, 1)
    print(var)
    listavar.append(var)

def p_allocatevar(p):
    '''allocatevar : empty'''
    var = listavar[len(listavar) - 1]
    listavar[len(listavar) - 1].updatememory(memoria.allocate(var.type, context, var.size))

def p_updatesize(p):
    '''updatesize : empty'''
    listavar[len(listavar) - 1].updatesize(p[-1])
    

def p_type(p):
    '''type : BOOLEAN settypebool
    | INTEGER settypeint
    | DECIMAL settypedec
    | STRING settypestring
    | FRACTION settypefrac'''
    print (p[0])

def p_assignment(p):
    '''assignment : ID pushid EQUALS expression SEMI updatevar'''
    print (p[0])

def p_updatevar(p):
    '''updatevar : empty'''
    tipoa = ptipos.pop()
    a = pilao.pop()
    tipob = ptipos.pop()
    b = pilao.pop()
    for v in listavar:
        if v.id == b:
            if v.type == tipoa:
                cuadruplo = Cuadruplo(18, a, None, v.memory)
                cuadruplos.append(cuadruplo)
            else:
                print ("Syntax error, trying to assign a different type to %s" % b)
        else:
            print ("Syntax error at, %s is not declared" % b)

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
    tipores = tipoResultante(tipob, tipoa, getNumOp(p[2]))
    if (tipores != -1):
        cuadruplo = Cuadruplo(getNumOp(p[2]), b, a, memoria.allocate(tipores, 20, 1))
        cuadruplos.append(cuadruplo)
        pilao.push(cuadruplo.pos4)
        ptipos.push(tipores)
    else:
        print ("Syntax error at '%s', incompatible types" % p[2])
        
def p_exp2(p):
    '''exp : ID pushdeclaredid
    | ID LBRACK expression RBRACK pushdeclaredid
    | LBRACK exp RBRACK
    | INTEGER_CONS settypeint pushcons
    | STRING_CONS settypestring pushcons 
    | FRACTION_CONS settypefrac pushcons 
    | DECIMAL_CONS settypedec pushcons 
    | TRUE settypebool pushcons
    | FALSE settypebool pushcons'''
    print (p[0])

def p_expunary(p):
    '''exp : EXMARK exp'''

    a = pilao.pop()
    tipoa = ptipos.pop()
    if (tipoa == 4):
        cuadruplo = Cuadruplo(14, a, None, memoria.allocate(4, 20))
        cuadruplos.append(cuadruplo)
        pilao.push(cuadruplo.pos4)
        ptipos.push(4)

def p_expgroup(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]

def p_pushtype(p):
    '''pushtype : empty'''
    print ("type:",type)
    global type
    tipo = [x.type for x in listavar if x.id == p[-1]]
    if tipo:
        ptipos.push(tipo[0])
    else:
        ptipos.push(type)
    print ("type:")
    print(type)

def p_pushid(p):
    '''pushid : pushtype'''
    pilao.push(p[-1])

def p_pushdeclaredid(p):
    '''pushdeclaredid : pushtype'''
    for v in listavar:
        if v.id == p[-1]:
            pilao.push(v.memory)
            return
    print ("Syntax error at '%s', variable not declared" % p[-1])
    sys.exit()

def p_pushcons(p):
    '''pushcons : pushtype'''
    if (type == 4) :
        if (p[-2] == "true"):
            memoria.allocateCons(4, 1)
        else:
            memoria.allocateCons(4, 0)
    else :
        pilao.push(memoria.allocateCons(type, p[-2]))
    
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
data = '''program a; function b (x : int, y : int) {
var dec x[5];
var dec y;
var string z;

z = "hello world";

x = 2+2;

if(x*2>0) {}
}
'''

t = yacc.parse(data)
print (t)
print (pilao)
print (ptipos)
print (len(cuadruplos))
print (listavar[1].type)
memoria.printVars()
for x in range (0, len(cuadruplos)) :
    print ('[',x+1,']',cuadruplos[x].pos1, ',' , cuadruplos[x].pos2,
        ',' ,cuadruplos[x].pos3, ',', cuadruplos[x].pos4)
