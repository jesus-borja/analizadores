# ----------------- Librerias Usadas ----------------- #
import re
from ply import lex
from ply.lex import Token

# ---------------------- TOKENS ---------------------- #

# Lista para almacenar los tokens no reconocidos
errores = []

# Palabras reservadas
keywords = [
    "FUNCTION",
    "ARROW", # nombre para "->"
    "IF",
    "ELSE",
    "FOR",
    "IN",
    "WHILE",
    "RETURN",
]

# Tipos de datos y literales
datatypes = [
    # Tipos de datos
    "TYPE_INTEGER",
    "TYPE_STRING",
    "TYPE_FLOAT",
    "TYPE_DOUBLE",
    "TYPE_BOOL",
    "TYPE_VOID",
    "TYPE_NULL",

    # Literales de datos
    "STRING",
    "INT",
    "FLOAT",
    "DOUBLE",
    "BOOL",
]

# Tabla de tokens
tokens = [
    "IDENTIFIER",

    # Operadores matemáticos
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "POWER",

    # Operadores lógicos
    # "EQUAL", # no se usa creo
    "ASSIGN_OP",
    "COMPARISON",
    "LESS_THAN",
    "GREATER_THAN",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    "NOT_EQUAL",
    "NOT",
    "AND",
    "OR",
    
    # Comentarios
    "COMMENT_START",
    "COMMENT_END",

    # Caracteres
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "SEMICOLON",
    "COMMA",
    "DOT",
    "COLON",

    # Otros
    "SPACE",
    "NEWLINE"
]

# Todos los tokens aceptados por el lexer
tokens = tokens + keywords + datatypes

# ---------------------- Expresiones Regulares "simples" ---------------------- #

# Operadores matemáticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'

# Operadores de asignación y comparación
t_ASSIGN_OP = r':='
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
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

# ----- Expresiones Regulares para tokens con mayor funcionalidad ----- #

# Tipos de datos
def t_TYPE_INTEGER(t):
    r'int'
    return t

def t_TYPE_STRING(t):
    r'str'
    return t
def t_TYPE_FLOAT(t):
    r'float'
    return t

def t_TYPE_DOUBLE(t):
    r'double'
    return t

def t_TYPE_BOOL(t):
    r'bool'
    return t

def t_TYPE_VOID(t):
    r'void'
    return t

def t_TYPE_NULL(t):
    r'null'
    return t

def t_ARROW(t):
    r'->'
    return t

def t_FLOAT(t):
    r'\d+\.\d+f'
    t.value = float(t.value[:-1]) # elimina la 'f' del final para tomar el valor del decimal
    return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value) # Convertir el valor del token a un entero
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1] # Eliminar las comillas del principio y del final
    return t

def t_BOOL(t):
    r'(true|false)'
    t.value = bool(t.value)
    return t

def t_FUNCTION(t):
    r'fun'
    return t

def t_RETURN(t):
    r'return'
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
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_COMMENT(t):
    r'/\?.*'
    pass

def t_SPACE(t):
    r'[^\S\n]'
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Se invoca la funcion cuando se da un caracter no reconocido
def t_error(t):
    global errores
    estado = "** El token no es válido en la línea {:4} Valor `{:16}` Posición {:4} Len: {:5}".format(str(t.lineno), str(t.value), str(t.lexpos), str(len(t.value)))
    errores.append(estado)
    # Salta el token y sigue con el resto de la entrada
    t.lexer.skip(1)

# ----- Funcionamiento del analizador léxico ----- #

# Creamos un lexer con la información de los tokens y expresiones regulares antes definidas
lexer = lex.lex()

# Prueba del lexer
lexer.input("""
fun factorial() -> void {
	x: int = 25;
	y: float = 2.3f;
	texto := 'cadena';

	if (y >= x) {
		print('Hola');
		return;
	} else {
		read(x);
		print(x);
	}

	/? comentario de bloque ?/
	xs := {21, 22, 23,}

	for x_ in xs {
		print(x_)
	}
	while true {
		print('a')
	}
}
""")

# Lee la entrada del lexer e imprime los tokens encontrados
while True:
    # Obtiene el siguiente token
    tok = lexer.token()
    # Cuando ya se consumió toda la entrada, se sale del ciclo
    if not tok:
        break
    # Prepara la linea con la informacion del token encontrado
    estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(
        str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
    print(estado)

# Se imprimen los errores encontrados (caracteres no reconocidos)
for e in errores:
    print(e)