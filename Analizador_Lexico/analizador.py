import re
from ply import lex
from ply.lex import Token

resultado_lexema = []

palabras_reservadas = {
    # Funciones
    'fun': 'FUNCTION',
    # Símbolos
    'returns': 'RETURN',
    # Estructuras de control
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'while': 'WHILE',
    # Tipos de datos
}

tokens = [
    "IDENTIFIER",

    # Operadores matemáticos
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",

    # Operadores lógicos
    "EQUAL",
    "ASSIGN_OP",
    "ASSIGN_OP_SHORT",
    "COMPARISON",
    "LESS_THAN",
    "GREATER_THAN",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    "NOT_EQUAL",
    "NOT",
    "AND",
    "OR",

    # Caracteres
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "LEFT_BRACE",
    "RIGHT_BRACE",

    #Valores
    "INTEGER",
    "STRING",
    # Otros
    "COMMMENT",
    "SPACE",
    "NEWLINE"

]
tokens = tokens + list(palabras_reservadas.values())

# Operadores matemáticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'

# Operadores de asignación y comparación
t_ASSIGN_OP = r':='
t_ASSIGN_OP_SHORT = r':'
t_COMPARISON = r'='

# Operadores de comparación
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_NOT_EQUAL = r'!='

# Operadores lógicos
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'

# Paréntesis, corchetes y llaves
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'

def t_RETURNS(t):
    r'returns'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor del token a un entero
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]  # Eliminar las comillas del principio y del final
    return t

def t_FUNCTION(t):
    r'fun'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_COMMENT(t):
    r'\?.*'
    pass

def t_SPACE(t):
    r'\t+'
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global resultado_lexema
    estado = "** El token no es válido en la línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


lexer = lex.lex()

# Prueba del lexer
lexer.input("""Mensaje: string = 'Hola' 
            if(Mensaje = 'Adios'){
            /? asfd
           Numero: int = 1
           }else {
            Numero.value: int = 2
           }
            """)

while True:
    tok = lexer.token()
    if not tok:
        break
    estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(
        str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
    print(estado)
