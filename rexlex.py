# -*- coding: utf-8 -*- 

###########################################################################
#   rexlex.py
#   Análisis léxico de Rex
#
#   Author: Andrés Alvarez
###########################################################################

import ply.lex as lex

keywords = {
    'var' : 'VAR',
    'int' : 'INTEGER',
    'dec' : 'DECIMAL',
    'fracc' : 'FRACTION',
    'string' : 'STRING',
    'program' : 'PROGRAM',
    'function' : 'FUNCTION',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'print' : 'PRINT',
    'or' : 'OR',
    'not' : 'NOT',
    'and' : 'AND',
    'return' : 'RETURN',
    'bool' : 'BOOLEAN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'void' : 'VOID',
    'do' : 'DO'
    }

tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MODULO', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'NEWLINE', 'COMMA', 'ID', 'SEMI', 'COLON',
    'RQUOTE', 'LQUOTE', 'LT', 'LE', 'GT', 'GE', 'NE', 'EXMARK', 'DECIMAL_CONS',
    'INTEGER_CONS', 'STRING_CONS', 'FRACTION_CONS', 'DIF', 'COMMENT', 'SAME'
    ]

tokens += keywords.values()


t_ignore = '\n \t'
t_EQUALS = r'='
t_SAME = r'=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_MODULO = r'%'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='
t_DIF = r'<>'
t_COMMA = r'\,'
t_SEMI = r';'
t_COLON = r':'
t_FRACTION_CONS = r'\d+\|d+'
t_STRING_CONS = r'\".*?\"'
t_EXMARK = r'!'
t_RQUOTE = r'"'
t_LQUOTE = r'."'
t_ignore_COMMENT = r'//'

###########################################################################
#   t_DECIMAL_CONS
#   Expresión regular para detectar los números con decimales
##########################################################################

def t_DECIMAL_CONS(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

###########################################################################
#   t_INTEGER_CONS
#   Expresión regular para detectar los números enteros
##########################################################################

def t_INTEGER_CONS(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t) :
    r'[a-z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)

