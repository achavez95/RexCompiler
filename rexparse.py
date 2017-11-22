# -*- coding: utf-8 -*-

#REX PARSER

###########################################################################
#SUMA = 0
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
#RETURN = 20
#PRINT = 21
#PARAM = 22
#ASSIGNCELL = 23
#ENDFUNC = 24
#ERA = 25
#INPUT = 26
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

data = None

tokens = rexlex.tokens
#Declaración de memoria compartida
class Memoria:
    #Inicialización de diccionario
    def __init__(self):
        self.memoria = {}
    #Mostrar todas las variables almacenadas
    def printVars(self):
        print("Variables en memoria", listavar)
        print("Variables de parametros")
        for f in range(0, len(listafunc)):
            print ("FUNCION", listafunc[f].id)
            print(listafunc[f].parameters)
        print("\n" + "MEMORIA" + "\n")
        iter = 0
        print(self.memoria.items())
            
    #Asigna una dirección de la memoria a una variable o valor temporal,
    #dependiendo del valor del contexto
    def allocate(self, tipo, context, size):
        #Variable que permite asignar direcciones
        #a diferentes tipos de contexto
        offset = 0 + 5000*context

        #Si la parte de la memoria no tiene el valor de "NI"
        #se sale del ciclo para asignar ese valor a la variable que lo pide
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
    #Asigna direcciones a constantes dependiendo del tipo
    def allocateCons(self, tipo, valor):
        
        if tipo == 0:
            #Si la direccion no esta en memoria, asignarle el valor de entrada al contador
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
    #Regresa el valor almacenado en una direccion
    def value(self, id):
        return self.memoria[id]
    #Actualiza el valor de una direccion dada
    def updateVar(self, id, value):
        self.memoria[id] = value
    #Borra la direccion de memoria dada
    def deleteVar(self, id):
        if id in self.memoria:
            del self.memoria[id]
    #Regresa el valor de retorno de la función ejecutandose (La utiliza la VM)
    def returnMem(self):
        returnmem = {}
        for id in self.memoria:
            if (id >= 300000):
                returnmem[id] = self.memoria[id]
        return returnmem
    #Regresa todas las variables temporales para almacenarlas antes de cambiar de funcion (La utiliza la VM)
    def getTemps(self):
        result = {}
        for key in range(100000, 105000):
            if key in self.memoria:
                print("GETTING TEMPS")
                result[key] = self.memoria[key]
        return result
    #Borra la memoria temporal al cambiar de funcion en compilacion
    def clearTemps(self):
        for key in range(100000, 105000):
            if key in self.memoria:
                del self.memoria[key]

                
#Inicialización de la memoria
memoria = Memoria()

#Función para reinicializar el parser para ejecutar otro codigo sin cerrar la VM
def reinitializeParser():
    global memoria
    global context
    global parametercount
    global type
    global asParameter
    global cuadruplos
    global pilao
    global ptipos
    global psaltos
    global listavar
    global listafunc
    global funcid
    
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
    funcid = None

#Variable global que indica el contexto actual (En este caso la variable en la que
#se encuentra la compilación
context = 0

#Variable global que indica el tipo actual de un estatuto, utilizado para declarar variables
type = None

#Conteo de parametros para la funcion actual
parametercount = 0

#Bandera que indica que las expresiones que se estan leyendo son parámetros
asParameter = False

#Lista de cuadruplos y pilas
cuadruplos = []
pilao = Stack()
ptipos = Stack()
psaltos = Stack()

#Lista de variables
listavar = []

#Lista de funcions
listafunc = []

#Id de la funcion actual en compilacion
funcid = None

#Precendecia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'EXMARK'),
    ('left', 'GT', 'LT', 'GE', 'LE', 'NE', 'SAME'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'POWER')
)

#Contenido de un programa
def p_program(p):
    '''program : PROGRAM ID SEMI gotomain program1
    | PROGRAM ID SEMI gotomain var program1'''
    print (p[0])

#Instruccion que inserta el primer goto al main
def p_gotomain(p):
    '''gotomain : empty'''
    cuadruplo = Cuadruplo(15, None, None, None)
    cuadruplos.append(cuadruplo)

#Funcion auxiliar para aceptar 1 o mas funciones
def p_program1(p):
    '''program1 : function program1
    | function'''

#Una funcion puede recibir parametros o no
def p_function(p):
    '''function : type FUNCTION ID pushid setcontext LPAREN parameter RPAREN savefunc block endfunc
    | type FUNCTION ID pushid setcontext LPAREN RPAREN savefunc block endfunc'''
    print ("FUNCTION READ")

#Instrucción que actualiza el context una vez leido un id de funcion nuevo
def p_setcontext(p):
    '''setcontext : empty'''
    global context
    context += 1

#Instrucción que se ejecuta al terminar parsear la funcion, limpia las temporales e inserta un
#ENDPROC a la lista de cuadruplos
def p_endfunc(p):
    '''endfunc : empty'''
    memoria.clearTemps()
    cuadruplo = Cuadruplo(24, None, None, None)
    cuadruplos.append(cuadruplo)
#Guarda la funcion y sus parametros en la lista de funciones
def p_savefunc(p):
    '''savefunc : empty'''
    print("PILAOATSAVEFUN:", pilao)
    print("PTIPOSATSAVEFUNC:", ptipos)
    listparam = []
    global cuadruplos
    #Ciclo que saca todos los parametros
    while pilao.size() > 1:
        tipo = ptipos.pop()
        param = pilao.pop()
        var = Variable(tipo, param, memoria.allocate(tipo, 2, 1), 1, 2, None)
        #El atributo parameters de Funcion es una lista de variables
        listparam.append(var)
    #Verificar si ya existe el id de la funcion
    if any(f.id == pilao.peek() for f in listafunc):
        print ("Syntax error, function %s has already been declared" % pilao.peek())
        sys.exit()
    #Asignar espacios de memoria a los parametros
    for p in listparam:
        p.updatememory(memoria.allocate(p.type, p.context, p.size))
    tipo = ptipos.pop()
    id = pilao.pop()
    #Actualizar el primer goto al encontrar la funcion main
    if id == "main":
        cuadruplos[0].pos4 = len(cuadruplos)
    print(listparam)
    #Crear el objeto de la funcion
    func = Function(tipo, id, listparam, len(listparam), len(cuadruplos), memoria.allocate(tipo, 60, 1), len(listparam))
    print("FRTN:", func.rtn)
    #Agregarla a la lista
    listafunc.append(func)


#Reglar para aceptar parametros
def p_parameter(p):
    '''parameter : type ID pushid
    | type ID pushid COMMA parameter'''
    print (p[0])
    
#Bloque principal de estatutos, utilizado por funciones
def p_block(p):
    '''block : LBRACE var vartoparam statements RBRACE deletelocal
    | LBRACE var vartoparam RBRACE deletelocal
    '''
    print (p[0])

#Elimina las variables locales una vez terminado de parsear el bloque
def p_deletelocal(p):
    '''deletelocal : empty'''
    for v in listafunc[context-1].parameters:
        memoria.deleteVar(v.memory)

#Agrega las variables locales declaradas dentro de una función a sus parametros para juntar todos en la misma
#variable local
def p_vartoparam(p):
    '''vartoparam : empty'''
    print("LISTAVAR:", listavar)
    for v in listavar:
        print("VAR TO PARAM")
        #si no es global agregarla a los parametros
        if v.context != 0:
            listafunc[context-1].parameters.append(v)
    listafunc[context-1].size = len(listafunc[context-1].parameters)
    #sacar la variable de la lista de variables
    for p in listafunc[context-1].parameters:
        for v in listavar:
            if p.id == v.id and p.context == v.context:
                listavar.remove(v)
#Bloque de estatutos sin variables declaradas           
def p_blocknovars(p):   
    '''block : LBRACE statements RBRACE
    | LBRACE RBRACE'''
#Bloque simple para condiciones y ciclos
def p_simpleblock(p):
    '''simpleblock : LBRACE statements RBRACE
    | LBRACE RBRACE'''

#Regla que evalue el tipo que se va a retornar contra el de la función
#si son el mismo se genera el cuadruplo RETURN
def p_savereturn(p):
    '''savereturn : empty'''
    
    print("PTIPOSATSAVE:", ptipos)
    global listafunc
    func = listafunc[context-1]
    #Si la funcion no es void
    if func.type != None:
        #Si son del mismo tipo
        if func.type == ptipos.peek():
            value = pilao.pop()
            print("PILAO:", value)
            print("VALUE:", memoria.value(value))
            #Cuadruplo RETURN
            cuadruplo = Cuadruplo(20, None, None, value)
            cuadruplos.append(cuadruplo)
            return
        else:
            print("Syntax error, returning a type different than the function's")
            sys.exit()
    else:
        print("Syntax error, return on a void function")
        sys.exit()
    
#Regla de estatutos
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
    | print SEMI
    | funcall SEMI
    | return SEMI
    | input SEMI'''
    print (p[0])

#Regla que inserta el cuadruplo INPUT a la lista de cuadruplos
def p_input(p):
    '''input : INPUT ID pushdeclaredid'''
    cuadruplo = Cuadruplo(26, ptipos.pop(), None, pilao.pop())
    cuadruplos.append(cuadruplo)

#Regla que inicia la funcionalidad de return, guardando el valor de la expresion en
#una variable
def p_return(p):
    '''return : RETURN expression savereturn 
    | RETURN savereturn'''
    
#Regla para insertar el cuadruplo PRINT
def p_print(p):
    '''print : PRINT expression'''
    print("PRINT")
    ptipos.pop()
    cuadruplo = Cuadruplo(21, None, None, pilao.pop())
    cuadruplos.append(cuadruplo)

#Regla para llamar una funcion
def p_funcall(p):
    '''funcall : CALL ID pushid LPAREN eragener startcount exparam RPAREN assignvalues
    | CALL ID pushid LPAREN eragener RPAREN assignvalues'''

#Regla que genera el cuadruplo ERA
def p_eragener(p):
    '''eragener : empty'''
    cuadruplo = Cuadruplo(25, context-1, None, None)
    cuadruplos.append(cuadruplo)

#Regla que indica que lo que va a seguir son parametros de una función
def p_startcount(p):
    '''startcount : empty'''
    global asParameter
    asParameter = True

#Regla que va contando el numero de parametros de entrada
def p_updatecount(p):
    '''updatecount : empty'''
    global parametercount
    parametercount += 1

#Regla que acepta los parametros y actualiza el contador
def p_exparam(p):
    '''exparam : expression updatecount
    | expression updatecount COMMA exparam'''

#Regla que asigna los valores de los parametros a las variables de la funcion
def p_assignvalues(p):
    '''assignvalues : empty'''
    
    global asParameter
    global pilao
    global ptipos
    asParameter = False
    #lista de parametros
    listparam = []
    #lista de tipos de los parametros
    listtype = []
    #Bandera para indicar que la funcion existe
    flag = False
    print ("PARAMETERCOUNT: ", parametercount)
    print("PILAOATCALL:", pilao)
    print("PTIPLOSATCALL:", ptipos)
    #Saca todos los parametros de las pilas
    for i in range(0, parametercount):
        listparam.append(pilao.pop())
        listtype.append(ptipos.pop())
    #Hace pop a la pila para obtener el id de la funcion
    id = pilao.pop()
    #Indica que la funcion actual ahora es id
    global funcid
    funcid = id
    print("FUNCID:", funcid)
    tipo = ptipos.pop()
    #Ciclo que genera los cuadruplos de PARAM para asignar valores a parametros
    for f in listafunc:
        if f.id == id:
            flag = True
            direc = f.dir
            if f.paramnumber == len(listparam):
                for i in range(0, f.paramnumber):
                    if listtype[i] == f.parameters[i].type:
                        cuadruplo = Cuadruplo(22, listparam[i], None, f.parameters[i].memory)
                        print("OP22:", cuadruplo)
                        cuadruplos.append(cuadruplo)
                    else:
                        print("Syntax error, type mismatch %s" % id)
                        sys.exit()
            else:
                print("Syntax error, invalid parameter number for function %s" % id)
                sys.exit()
    if not flag:
        print("%s function not declared" % id)
        sys.exit()
    #Una vez finalizada la asignacion de parametros, llama a la funcion para ejecutar
    cuadruplo = Cuadruplo(19, None, None, direc)
    cuadruplos.append(cuadruplo)
    global parametercount
    parametercount = 0
    return
        
    print("Syntax error, no function called %s" % id)
    sys.exit()
 #Regla de for (NO IMPLEMENTADO)                       
def p_for(p):
    '''for : LPAREN assignment expression SEMI expression RPAREN simpleblock'''
    print (p[0])
#Regla de do while
def p_dowhile(p) :
    '''dowhile : DO pushjump simpleblock WHILE LPAREN expression RPAREN gotot'''
    print (p[0])
#Regla que inserta el numero de cuadruplo actual a la pila de saltos
def p_pushjump(p) :
    '''pushjump : empty'''
    psaltos.push(len(cuadruplos))
#Regla que genera el cuadruplo para GOTOT
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

#Regla de while
def p_while(p):
    '''while : WHILE pushjump LPAREN expression RPAREN gotof simpleblock gotowhile'''
    print (p[0])

#Regla que inserta un cuadruplo GOTO para hacer el ciclo 
def p_gotowhile(p):
    '''gotowhile : empty'''
    index = psaltos.pop()
    jump = psaltos.pop()
    cuadruplo = Cuadruplo(15, None, None, jump)
    cuadruplos.append(cuadruplo)
    cuadruplos[index].updatedir(len(cuadruplos))

#Regla de condition, puede tener else o no
def p_condition(p):
    '''condition : IF LPAREN expression RPAREN gotof simpleblock ELSE gotoif simpleblock updatejump
    | IF LPAREN expression RPAREN gotof simpleblock updatejump'''
    print (p[0])
    
#Generación de cuadruplo goto para IF
def p_gotoif(p):
    '''gotoif : empty'''
    cuadruplo = Cuadruplo(15, None, None, None)
    cuadruplos.append(cuadruplo)
    index = psaltos.pop()
    cuadruplos[index].updatedir(len(cuadruplos))
    psaltos.push(len(cuadruplos) - 1)

#Generacion de cuadruplo gotoF utilizado por while e if
def p_gotof(p):
    '''gotof : empty'''
    a = pilao.pop()
    tipoa = ptipos.pop()
    #Si el tipo de la expresion es bool
    if (tipoa == 4) :
        cuadruplo = Cuadruplo(17, a, None, None)
        cuadruplos.append(cuadruplo)
        psaltos.push(len(cuadruplos) - 1)
    else:
        print ("Syntax error at '%s', incompatible types" % p[-1])

#Actualiza el cuadruplo con direccion a saltar pendiente
def p_updatejump(p):
    '''updatejump : empty'''
    index = psaltos.pop()
    cuadruplos[index].updatedir(len(cuadruplos))

#Regla de declaracion de variables
def p_var(p):
    '''var : VAR type var1 SEMI var
    | VAR type var1 SEMI'''
    print (p[0])

#Regla auxiliar que permite declarar arreglos
def p_var1(p):
    '''var1 : ID pushid savevar allocatevar
    | ID pushid savevar allocatevar COMMA var1
    | ID pushid savevar LBRACK INTEGER_CONS updatesize RBRACK allocatevar COMMA var1
    | ID pushid savevar LBRACK INTEGER_CONS updatesize RBRACK allocatevar'''
    print (p[0])
#Indica al parser que las variables que siguen son int
def p_settypeint(p):
    '''settypeint : empty'''
    global type
    type = 0
#Indica al parser que las variables que siguen son dec
def p_settypedec(p):
    '''settypedec : empty'''
    global type
    type = 1
#Indica al parser que las variables que siguen son fracc
def p_settypefrac(p):
    '''settypefrac : empty'''
    global type
    type = 2
#Indica al parser que las variables que siguen son string
def p_settypestring(p):
    '''settypestring : empty'''
    global type
    type = 3
#Indica al parser que las variables que siguen son bool
def p_settypebool(p):
    '''settypebool : empty'''
    global type
    type = 4
#Indica que lo que sigue es void
def p_settypevoid(p):
    '''settypevoid : empty'''
    global type
    type = None

#Guarda la variable en la lista de variables
def p_savevar(p):
    '''savevar : empty'''
    id = pilao.pop()
    tipo = ptipos.pop()
    tipo = type
    exist = True
    global con
    con = 0
    #Si no estamos en el contexto global
    if context != 0:
        con = 2
        #Si no hay variable con este id en las variables locales de la funcion
        for v in listafunc[context-1].parameters:
            if not v.id == id:
                exist = True
                break;
            exist = False
    else:
        #Si no existe el id en las variables globales
        for v in listavar:
            if not v.id == id:
                exist = True
                break;
            exist = False

    if not exist:
        print("Syntax error, variable %s already declared on this scope" %id)
        sys.exit()
    
    print("ID: ", id)
    #Crea la variable y la mete a la lista
    var = Variable(tipo, id, None, 1, con, None)
    listavar.append(var)
    
#Le da una dirección a la variable dependiendo del contexto en el que se declaro
def p_allocatevar(p):
    '''allocatevar : empty'''
    var = listavar[len(listavar) - 1]
    listavar[len(listavar) - 1].updatememory(memoria.allocate(var.type, con, var.size))

#Actualiza el tamaño de la variable una vez que se obtiene el tamaño
def p_updatesize(p):
    '''updatesize : empty'''
    listavar[len(listavar) - 1].updatesize(p[-1])
    
#Regla que acepta el tipo de datos y actualiza la variable global type
def p_type(p):
    '''type : BOOLEAN settypebool
    | INTEGER settypeint
    | DECIMAL settypedec
    | STRING settypestring
    | FRACTION settypefrac
    | VOID settypevoid'''
    print ("TYPE SET: ", type)

#Regla que permite asignar valores a variables
def p_assignment(p):
    '''assignment : ID pushid EQUALS expression SEMI updatevar
    | ID pushid LBRACK expression RBRACK EQUALS expression SEMI updatecell'''
    print (p[0])

#Regla que permite actualizar celdas de arreglos
def p_updatecell(p):
    '''updatecell : empty'''
    #3 valores, lo que se va a asignar, la variable y el indice
    tipoa = ptipos.pop()
    a = pilao.pop()
    print("A: ", a)
    tipob = ptipos.pop()
    b = pilao.pop()
    tipoc = ptipos.pop()
    c = pilao.pop()

    #si el indice es int
    if tipob == 0:
        for v in listavar:
            if v.type == tipoa:
                #si la variable existe
                if v.id == c:
                    direc = memoria.allocate(0, 20, 1)
                    memoria.updateVar(direc, v.memory)
                    
                    cuadruplo = Cuadruplo(0, b, direc, memoria.allocate(0, 20, 1))
                    cuadruplos.append(cuadruplo)
                    #Cuadruplo para asignar a una celda, es diferente porque se tiene que calcular
                    #la direccion de la celda y ese calculo es la direccion de una direccion
                    cuadruploaux = Cuadruplo(23, a, None, cuadruplo.pos4)
                    cuadruplos.append(cuadruploaux)
        #El mismo ciclo de arriba pero para variables locales
        for v in listafunc[context-1].parameters:
            if v.type == tipoa:
                if v.id == c:
                    direc = memoria.allocate(0, 20, 1)
                    memoria.updateVar(direc, v.memory)
                    
                    cuadruplo = Cuadruplo(0, b, direc, memoria.allocate(0, 20, 1))
                    cuadruplos.append(cuadruplo)
                    cuadruploaux = Cuadruplo(23, a, None, cuadruplo.pos4)
                    cuadruplos.append(cuadruploaux)
#Actualiza el valor de una variable
def p_updatevar(p):
    '''updatevar : empty'''
    print("PILAOUPDATE:", pilao)
    print("PTIPOSUPDATE:", ptipos)
    tipoa = ptipos.pop()
    a = pilao.pop()
    tipob = ptipos.pop()
    print(a)
    b = pilao.pop()
    print(listavar)
    #Si existe en las variableslocales
    for v in listafunc[context-1].parameters:
        if v.id == b:
            #Si sus tipos son iguales
            if v.type == tipoa:
                #Genera cuadruplo de asignacion
                cuadruplo = Cuadruplo(18, a, None, v.memory)
                cuadruplos.append(cuadruplo)
                print(cuadruplo)
                return
    #Si existe en las globales
    for v in listavar:
        print("HELLO")
        if v.id == b:
            if v.type == tipoa:
                cuadruplo = Cuadruplo(18, a, None, v.memory)
                cuadruplos.append(cuadruplo)
                print(cuadruplo)
                return
            else:
                print ("Syntax error, trying to assign a different type to %s" % b)
        else:
            print ("Syntax error at, %s is not declared" % b)

#Regla que acepta expresiones 
def p_expression(p):
    '''expression : exp
    '''
    print (p[0])

#Regla que inserta cuadruplos a la lista de cuadruplos dependiendo de la operacion
#sigue la precedencia declarada al principio
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
    #Valida la operacion con el cubo de operaciones
    tipores = tipoResultante(tipob, tipoa, getNumOp(p[2]))
    if (tipores != -1):
        #Genera el cuadruplo de operacion
        cuadruplo = Cuadruplo(getNumOp(p[2]), b, a, memoria.allocate(tipores, 20, 1))
        cuadruplos.append(cuadruplo)
        pilao.push(cuadruplo.pos4)
        ptipos.push(tipores)
        print("ASPARAM:", asParameter)
    else:
        print ("Syntax error at '%s', incompatible types" % p[2])
#Regla que acepta exp individuales
def p_exp2(p):
    '''exp : ID pushdeclaredid
    | ID pushdeclaredid LBRACK expression RBRACK pushdeclaredarray
    | LBRACK exp RBRACK
    | INTEGER_CONS settypeint pushcons
    | STRING_CONS settypestring pushcons 
    | FRACTION_CONS settypefrac pushcons 
    | DECIMAL_CONS settypedec pushcons 
    | TRUE settypebool pushcons
    | FALSE settypebool pushcons'''
    print ("DECLARED:", asParameter)
#Operaciones unarias
def p_expunary(p):
    '''exp : EXMARK exp'''

    a = pilao.pop()
    tipoa = ptipos.pop()
    if (tipoa == 4):
        cuadruplo = Cuadruplo(14, a, None, memoria.allocate(4, 20))
        cuadruplos.append(cuadruplo)
        pilao.push(cuadruplo.pos4)
        ptipos.push(4)
#Parentesis para obligar a ejecutar primero
def p_expgroup(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]
#Llamada de funcion para realizar operaciones con el resultado
def p_expfunc(p):
    '''exp : funcall pushrtn'''
    for f in listafunc:
        if f.id == funcid:
            ptipos.push(f.type)
#Mete a la pila de operadores la direccion de retorno de la funcion para seguir con la operacion
#despues de la llamada
def p_pushrtn(p):
    '''pushrtn : empty'''
    pilao.push(memoria.allocate(ptipos.peek(), 20, 1))
    for f in listafunc:
        if f.id == funcid:
            cuadruplo = Cuadruplo(18, f.rtn, None, pilao.peek())
            cuadruplos.append(cuadruplo)
            break
    print ("PUSHRTN: ", context-1)

#Mete el tipo de un id o constante a la pila
def p_pushtype(p):
    '''pushtype : empty'''
    print ("type:",type)
    global type
    tipo = [x.type for x in listavar if x.id == p[-1]]
    tipob = None
    if listafunc:
        tipob = [x.type for x in listafunc[context-1].parameters if x.id == p[-1]]
    if tipo:
        ptipos.push(tipo[0])
    elif tipob:
        ptipos.push(tipob[0])
    else:
        ptipos.push(type)
    print ("type:", ptipos)

#Mete cualquier id a la pila
def p_pushid(p):
    '''pushid : pushtype'''
    print("ID PUSHED: ", p[-1])
    pilao.push(p[-1])
#Mete un id declarado anteriormente a la pila
def p_pushdeclaredid(p):
    '''pushdeclaredid : pushtype'''
    print("PUSHDECLAREDID")
    for v in listavar:
        if v.id == p[-1]:
            if v.size > 1:
                pilao.push(v.id)
            else:
                pilao.push(v.memory)
            return
    for v in listafunc[context-1].parameters:
        if v.id == p[-1]:
            if v.size > 1:
                pilao.push(v.id)
            else:
                pilao.push(v.memory)
            return
    print ("Syntax error at '%s', variable not declared" % p[-1])
    sys.exit()
#Mete un arreglo declarado anteriormente a la pila
def p_pushdeclaredarray(p):
    '''pushdeclaredarray : pushtype'''
    cell = pilao.pop()
    tipocell = ptipos.pop()
    id = pilao.pop()
    if tipocell == 0:
        for v in listavar:
            if v.id == id:
                pilao.push(cell)
                return
        for v in listafunc[context-1].parameters:
            if v.id == id:
                pilao.push(cell)
                return
    print ("Syntax error at '%s', variable not declared" % p[-1])
    sys.exit()
#Mete la direccion de la constante a la pila
def p_pushcons(p):
    '''pushcons : pushtype'''
    if (type == 4) :
        if (p[-2] == "true"):
            memoria.allocateCons(4, 1)
        else:
            memoria.allocateCons(4, 0)
    else :
        pilao.push(memoria.allocateCons(type, p[-2]))
    print("PUSHCONS: ", p[-2])
    print(p[-2])

#Regla para indicar que no espera nada la regla
def p_empty(p):
    '''empty :'''
    pass

#Error de sintaxis
def p_error(p):
    if p:
        print ("Sintax error at '%s'" % p.value)
        sys.exit()
    else:
        print ("Syntax error at EOF")


yacc.yacc()

# data = 'program a; void function b () { var x : int; } '
#data = '''program a;
#var int c;
#int function asd (int x, dec y) {
#    var int a;
#    return 5*x;
#    a = asd(5, 1.0);
#    return x;
#}
#
#void function foo (int x) {
#    var int f;
#    f = asd(3, 5.0);
#}
#'''

