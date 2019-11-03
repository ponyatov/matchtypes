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

# NLTK:
## lemmatizer
# https://nlpub.mipt.ru/Pymorphy

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# https://www.dabeaz.com/ply/ply.html
# https://www.matthieuamiguet.ch/media/documents/TeachingCompilersWithPython_Slides.pdf

## lexer part (single tokens)

import ply.lex  as lex

# lexer token classes
tokens = ['w','p','eol']#,'n'

t_ignore = ' \t'

def t_eol(t):
    r'[\r\n]+'
    t.value = '\n' ; return t

# plus
def t_p(t):
    r'\+'
    return t

# numbers
def t_n(t):
    r'[0-9]+'
    # no return: ignore

# word (^ not ignore + plus)
def t_w(t):
    r'[^ \t\r\n]+'
    t.value = morph.parse(t.value)[0].normal_form
    return t

def t_error(t): raise SyntaxError(t)    

lexer = lex.lex()


## parser part (tokens groups & syntax)

import ply.yacc as yacc

accum = []

def p_repl_empty(p):
    ' repl : '
    pass

def p_repl_plused(p):
    ' repl : repl p w '
    global accum ; accum += [(p[2],p[3])]

def p_repl_single(p):
    ' repl : repl w '
    global accum ; accum += [(p[2])]

def p_repl_eol(p):
    ' repl : repl eol '
    global accum
    if accum: print(accum) ; accum = []

def p_error(p): raise SyntaxError(p)    

parser = yacc.yacc(debug=False,write_tables=False)


if __name__ == '__main__':
    parser.parse(src)
    # lexer.input(src)
    # while True:
    #     token = lexer.token()
    #     if not token: break
    #     print(token)
