#An implementation of Rex

from ply import *
import rexlex

token = rexlex.tokens

precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'times', 'divide', 'modulo')
    ('left', 'power'),
    ('right', 'uminus')
)

#A Rex program is a series of statements.

def p_program(p) :
    if p[0] = 
