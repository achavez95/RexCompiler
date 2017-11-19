# -*- coding: utf-8 -*- 

###########################################################################
#   SUMA = 0
#RESTA = 1
#MULTIPLICACION = 2
#DIVISION = 3
#MODULO = 4
#POTENCIA = 5
#MENORQUE = 6
#MENORIGUAL = 7
#MAYORQUE = 8
#MAYORIGUAL = 9
#DIFERENTE = 10
#IGUAL = 11
#AND = 12
#OR = 13
#NOT = 14
#GOTO = 15
#GOTOT = 16
#GOTOF = 17
#ASSIGN = 18
#CALL = 19
#   Author: Andrés Alvarez
##########################################################################

from ply import *
import rexlex
from cubo import *
from stack import *
from cuadruplo import *
from variable import *
from function import *
import sys

tokens = rexlex.tokens

class Memoria:
    def __init__(self):
        self.memoria = {}

    def printVars(self):
        print("Variables en memoria", listavar)
        print("\n" + "MEMORIA" + "\n")
        iter = 0
        print(self.memoria.items())
            

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

    def value(self, id):
        return self.memoria[id]

    def updateVar(self, id, value):
        self.memoria[id] = value

    def deleteVar(self, id):
        if id in self.memoria:
            del self.memoria[id]

memoria = Memoria()

context = 0

type = None

parametercount = 0

asParameter = False

#Lista de cuadruplos y pilas
cuadruplos = []
pilao = Stack()
ptipos = Stack()
psaltos = Stack()

#Lista de variables
listavar = []

listafunc = []

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
    '''program : PROGRAM ID SEMI program1
    | PROGRAM ID SEMI var program1'''
    print (p[0])

def p_program1(p):
    '''program1 : function program1
    | function'''

def p_function(p):
    '''function : type FUNCTION ID pushid LPAREN parameter RPAREN savefunc block
    | type FUNCTION ID pushid LPAREN RPAREN savefunc block'''
    print (p[0])

def p_savefunc(p):
    '''savefunc : empty'''
    listparam = []
    while pilao.size() > 1:
        tipo = ptipos.pop()
        param = pilao.pop()
        var = Variable(tipo, param, None, 1, context+1)
        listparam.append(var)
    if any(f.id == pilao.peek() for f in listafunc):
        print ("Syntax error, function %s has already been declared" % pilao.peek())
        sys.exit()
    for p in listparam:
        p.updatememory(memoria.allocate(p.type, p.context, p.size))
    tipo = ptipos.pop()
    id = pilao.pop()
    print(listparam)
    func = Function(tipo, id, listparam, len(cuadruplos))
    listafunc.append(func)
    global context
    context += 1

def p_parameter(p):
    '''parameter : type ID pushid
    | type ID pushid COMMA parameter'''
    print (p[0])

def p_block(p):
    '''block : LBRACE statements RETURN expression SEMI savereturn RBRACE
    | LBRACE RETURN expression SEMI savereturn RBRACE
    | LBRACE statements nortn RBRACE
    | LBRACE nortn RBRACE
    '''
    print (p[0])

def p_blocknortn(p):
    '''blocknortn : LBRACE statements RBRACE
    | LBRACE RBRACE'''

def p_nortn(p):
    '''nortn : empty'''
    func = listafunc[context-1]
    if func.type != None:
        print("Syntax error, missing return on function %s" % func.id)
        sys.exit()

def p_savereturn(p):
    '''savereturn : empty'''
    func = listafunc[context-1]
    if func.type != None:
        if func.type == ptipos.peek():
            return
        else:
            print("Syntax error, returning a type different than the function's")
            sys.exit()
    else:
        print("Syntax error, return on a void function")
        sys.exit()
    

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
    | print
    | var
    | funcall'''
    print (p[0])

def p_print(p):
    '''print : PRINT LPAREN expression RPAREN SEMI
    | PRINT LPAREN STRING_CONS RPAREN SEMI
    | PRINT LPAREN ID RPAREN SEMI'''

def p_funcall(p):
    '''funcall : ID pushid LPAREN startcount expression exparam RPAREN assignvalues SEMI
    | ID pushid RPAREN LPAREN assignvalues SEMI'''

def p_startcount(p):
    '''startcount : empty'''
    global asParameter
    asParameter = True

def p_exparam(p):
    '''exparam : COMMA expression exparam
    | COMMA expression'''

def p_assignvalues(p):
    '''assignvalues : empty'''
    
    global asParameter
    asParameter = False
    listparam = []
    listtype = []
    print ("PARAMETERCOUNT: ", parametercount)
    for i in range(0, parametercount):
        
        listparam.append(pilao.pop())
        listtype.append(ptipos.pop())
    id = pilao.pop()
    tipo = ptipos.pop()
    
    for f in listafunc:
        if f.id == id:
            if len(f.parameters) == len(listparam):
                for i in range(0, len(f.parameters)):
                    if listtype[i] == f.parameters[i].type:
                        
                        memoria.updateVar(f.parameters[i].memory, memoria.value(listparam[i]))
    

def p_for(p):
    '''for : LPAREN assignment expression SEMI expression RPAREN blocknortn'''
    print (p[0])

def p_dowhile(p) :
    '''dowhile : DO pushjump blocknortn WHILE LPAREN expression RPAREN gotot'''
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
    '''while : WHILE pushjump LPAREN expression RPAREN gotof blocknortn gotowhile'''
    print (p[0])

def p_gotowhile(p):
    '''gotowhile : empty'''
    index = psaltos.pop()
    jump = psaltos.pop()
    cuadruplo = Cuadruplo(15, None, None, jump)
    cuadruplos.append(cuadruplo)
    cuadruplos[index].updatedir(len(cuadruplos) + 1)

def p_condition(p):
    '''condition : IF LPAREN expression RPAREN gotof blocknortn ELSE gotoif blocknortn updatejump
    | IF LPAREN expression RPAREN gotof blocknortn updatejump'''
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

def p_settypevoid(p):
    '''settypevoid : empty'''
    global type
    type = None

def p_savevar(p):
    '''savevar : empty'''
    id = pilao.pop()
    tipo = ptipos.pop()
    tipo = type
    for v in listavar:
        if v.id == id:
            listavar.remove(v)
            memoria.deleteVar(v.memory)
    if context != 0:
        for v in listafunc[context-1].parameters:
            if v.id == id:
                memoria.deleteVar(v.memory)
    print("ID: ", id)
    var = Variable(tipo, id, None, 1, context)
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
    | FRACTION settypefrac
    | VOID settypevoid'''
    print ("TYPE SET: ", type)

def p_assignment(p):
    '''assignment : ID pushid EQUALS expression SEMI updatevar
    | ID pushid LBRACK expression RBRACK EQUALS expression SEMI updatecell'''
    print (p[0])

def p_updatecell(p):
    '''updatecell : empty'''
    tipoa = ptipos.pop()
    a = pilao.pop()
    print("A: ", a)
    tipob = ptipos.pop()
    b = pilao.pop()
    tipoc = ptipos.pop()
    c = pilao.pop()

    if tipob == 0:
        for v in listavar:
            if v.type == tipoa:
                if v.id == c:
                    cuadruplo = Cuadruplo(0, b, v.memory, memoria.allocate(0, 20, 1))
                    cuadruplos.append(cuadruplo)
                    cuadruploaux = Cuadruplo(18, a, None, memoria.value(cuadruplo.pos4))
                    cuadruplos.append(cuadruploaux)

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
        print("ASPARAM: ", asParameter)
        if asParameter:
            global parametercount
            parametercount += 1
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
    if asParameter:
            global parametercount
            parametercount += 1
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
    print("ID PUSHED: ", p[-1])
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

# data = 'program a; void function b () { var x : int; } '
data = '''program a;
var int c;
void function ax (int x, dec y) {
var int z;
z = 2*50;

if (z>10) {}

ax(4, 4.5);
}
'''

t = yacc.parse(data)
print (t)
print (pilao)
print (ptipos)
print (len(cuadruplos))
memoria.printVars()
for x in range (0, len(cuadruplos)) :
    print ('[',x+1,']',cuadruplos[x].pos1, ',' , cuadruplos[x].pos2,
        ',' ,cuadruplos[x].pos3, ',', cuadruplos[x].pos4)
