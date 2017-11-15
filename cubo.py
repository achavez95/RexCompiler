# -*- coding: utf-8 -*- 

###########################################################################
#   cubo.py
#   Cubo de operaciones
#
#   Author: Andrés Alvarez
##########################################################################

# Operadores
INT = 0
DEC = 1
FRAC = 2
STRING = 3
BOOLEAN = 4
ERROR = -1
#VOID = 5

# Identificadores de operadores
SUMA = 0
RESTA = 1
MULTIPLICACION = 2
DIVISION = 3
MODULO = 4
POTENCIA = 5
MENORQUE = 6
MENORIGUAL = 7
MAYORQUE = 8
MAYORIGUAL = 9
DIFERENTE = 10
IGUAL = 11
AND = 12
OR = 13

###########################################################################
#   getNumOp
#   Obtiene el numero de operación de un operador
##########################################################################
def getNumOp(op):
    if op == '+':
        return SUMA
    elif op == '-':
        return RESTA
    elif op == '*':
        return MULTIPLICACION
    elif op == '/':
        return DIVISION
    elif op == '%':
        return MODULO
    elif op == '^':
        return POTENCIA
    elif op == '<':
        return MENORQUE
    elif op == '<=':
        return MENORIGUAL
    elif op == '>':
        return MAYORQUE
    elif op == '>=':
        return MAYORIGUAL
    elif op == '!=':
        return DIFERENTE
    elif op == '==':
        return IGUAL
    elif op == '&&':
        return AND
    elif op == '||':
        return OR
    else:
        return -1


#Declaración del cubo semántico de operadores
CUBO = [
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, -1, -1],
    [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, -1, -1],
    [2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, -1, -1],
    [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, -1, -1],
    [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, -1, -1],
    [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, -1, -1],
    [2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4] ]

###########################################################################
#   tipoResultante
#   Obtiene el tipo resultante de la operación de dos tipos
##########################################################################

def tipoResultante (operando1, operando2, operador):
    reng = operando1 * 5 + operando2
    colu = operando2 + 2
    return CUBO[reng][colu]
