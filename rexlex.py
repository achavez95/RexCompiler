# Implementation of Rex 

import ply.lex as lex

keywords = (
    'var', 'integer', 'decimal', 'fraction', 'string', 'program', 'function',
    'if', 'else', 'for', 'while', 'print', 'or', 'not', 'and', 'return', 'boolean',
    )

tokens = keywords + (
    'equals', 'plus', 'minus', 'times', 'divide', 'power', 'modulo', 'lparen', 'rparen',
    'lbrace', 'rbrace', 'lbrack', 'rbrack', 'newline', 'comma', 'id', 'semi',
    'rquote', 'lquote', 'lt', 'le', 'gt', 'ge', 'ne', 'exmark',
    )

def t_ID(t) :
    r'[a-z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t

t_equals = r'='
t_plus = r'\+'
t_minus = r'-'
t_times = r'\*'
t_power = r'\*\*'
t_divide = r'/'
t_lparen = r'\('
t_rparen = r'\)'
t_lbrack = r'\['
t_rbrack = r'\]'
t_lbrace = r'\{'
t_rbrace = r'\}'
t_lt = r'<'
t_le = r'<='
t_gt = r'>'
t_ge = r'>='
t_ne = r'<>'
t_comma = r'\,'
t_semi = r';'
t_integer = r'\d+'
t_decimal = r'(\d*\.\d+)'
t_fraction = r'(\d+\/\d+)'
t_string = r'\".*?\"'
t_exmark = r'!'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)


lex.lex(debug=0)
