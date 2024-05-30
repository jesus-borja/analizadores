import ply.lex as lex

# Lista para almacenar los tokens no reconocidos
errores = []

# Palabras reservadas
keywords = {
    "fun": "FUNCTION",
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "in": "IN",
    "while": "WHILE",
    "return": "RETURN",
    "int": "TYPE_INTEGER",
    "str": "TYPE_STRING",
    "float": "TYPE_FLOAT",
    "double": "TYPE_DOUBLE",
    "bool": "TYPE_BOOL",
    "void": "TYPE_VOID",
    "null": "TYPE_NULL",
}

# Lista de tokens
tokens = [
    "IDENTIFIER", "INT", "FLOAT", "DOUBLE", "STRING", "BOOL",
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MODULO", "POWER",
    "ASSIGN_OP", "COMPARISON", "LESS_THAN", "GREATER_THAN",
    "GREATER_EQUAL", "LESS_EQUAL", "NOT_EQUAL", "NOT", "AND", "OR",
    "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET",
    "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", "COMMA", "DOT", "COLON", "ARROW",
] + list(keywords.values())

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN_OP = r'='
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COMPARISON = r'=='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_NOT_EQUAL = r'!='
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_ARROW = r'->'

# Tipos de datos y literales
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

def t_BOOL(t):
    r'\btrue\b|\bfalse\b'
    t.value = (t.value == 'true')
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Ignorar comentarios
def t_COMMENT(t):
    r'/\?.*'
    pass

# Ignorar espacios y tabs
t_ignore = ' \t'

# Ignorar nuevas líneas y actualizar el número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Se invoca la función cuando se da un caracter no reconocido
def t_error(t):
    global errores
    estado = "** El token no es válido en la línea {:4} Valor `{:16}` Posición {:4} Len: {:5}".format(str(t.lineno), str(t.value), str(t.lexpos), str(len(t.value)))
    errores.append(estado)
    t.lexer.skip(1)

# Construir el analizador léxico
analizador = lex.lex()