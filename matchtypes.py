# https://tools.yaroshenko.by/matchtypes.php

src = '''
ремонт квартир +в москве	8 168
ремонт квартиры москва цены	1 160
ремонт квартир под ключ москва	862
частный ремонт квартир +в москве	 337
'''

dst = '''
+ремонт +квартир +в +москве
[ремонт квартир в москве]
+ремонт +квартиры +москва +цены
[ремонт квартиры москва цены]
+ремонт +квартир +под +ключ +москва
[ремонт квартир под ключ москва]
+частный +ремонт +квартир +в +москве
[частный ремонт квартир в москве]
'''

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['c']

t_ignore = ' \t\r\n'

def t_c(t):
    r'.'
    return t

def t_error(t): raise SyntaxError(t)    

lexer = lex.lex()

if __name__ == '__main__':
    lexer.input(src)
    while True:
        token = lexer.token()
        if not token: break
        print(token)
