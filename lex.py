from ply.lex import lex
import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'IF',
    'ELSE',
    'WHILE',
    'EQUALS',
    'COMPARISON',
    'LBRACE',
    'RBRACE'
)

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_EQUALS   = r'='
t_COMPARISON = r'==|!=|<=|>=|<|>'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') 
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def test_lexer(input_string):
    lexer.input(input_string)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == '__main__':
    print("Probando lexer (escribe 'salir' para terminar):")
    while True:
        data = input("> ")
        if data.lower() == 'salir':
            break
        test_lexer(data)
