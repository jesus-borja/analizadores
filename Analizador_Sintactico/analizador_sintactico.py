import ply.yacc as yacc
from analizador_lexico import tokens, analizador

# Definir las reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('right', 'POWER'),
    ('left', 'COMPARISON', 'LESS_THAN', 'GREATER_THAN', 'GREATER_EQUAL', 'LESS_EQUAL', 'NOT_EQUAL'),
    ('right', 'NOT'),
    ('left', 'AND', 'OR'),
)

# Diccionario para almacenar los valores de las variables
variables = {}
resultado_gramatica = []


# Definir las funciones correspondientes a cada regla de producción

def p_F(p):
    '''F : LEFT_PAREN E RIGHT_PAREN
         | IDENTIFIER
         | INT
         | FLOAT
         | DOUBLE
         | STRING
         | BOOL
         | NOT E
         | E COMPARISON E
         | E LESS_THAN E
         | E GREATER_THAN E
         | E LESS_EQUAL E
         | E GREATER_EQUAL E
         | E NOT_EQUAL E
         | E AND E
         | E OR E'''
    if len(p) == 2:  # IDENTIFIER, INT, FLOAT, DOUBLE, STRING, BOOL
        if isinstance(p[1], str) and p[1] in variables:
            p[0] = variables[p[1]]
        else:
            p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    elif p[1] == '!':
        p[0] = not p[2]
    elif len(p) == 4:
        if p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
        elif p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '&&':
            p[0] = p[1] and p[3]
        elif p[2] == '||':
            p[0] = p[1] or p[3]

def p_E(p):
    '''E : F'''
    p[0] = p[1]

def p_expression_plus(p):
    'E : E PLUS E'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'E : E MINUS E'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'E : E TIMES E'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'E : E DIVIDE E'
    p[0] = p[1] / p[3]

def p_expression_modulo(p):
    'E : E MODULO E'
    p[0] = p[1] % p[3]

def p_expression_power(p):
    'E : E POWER E'
    p[0] = p[1] ** p[3]
  
def p_VD(p):
    'VD : IDENTIFIER COLON TD ASSIGN_OP E'
    variables[p[1]] = p[5]  # Almacena el valor de la variable en el diccionario


def p_TD(p):
    '''TD : TYPE_BOOL 
          | TYPE_DOUBLE
          | TYPE_FLOAT
          | TYPE_INTEGER
          | TYPE_NULL
          | TYPE_STRING
          | TYPE_VOID'''
    p[0] = p[1]

def p_FD(p):
    'FD : FUNCTION IDENTIFIER LEFT_PAREN PL RIGHT_PAREN ARROW TD B'
    # Define una función para esta producción
    pass

def p_S(p):
    '''S : E SEMICOLON
         | IfS
         | WS
         | FS
         | RS
         | VD SEMICOLON'''

def p_B(p):
    'B : LEFT_BRACKET SL RIGHT_BRACKET'

def p_SL(p):
    '''SL : S
          | SL S''' 

def p_PL(p):
    '''PL : PL COMMA IDENTIFIER COLON TD
          | IDENTIFIER COLON TD'''       

def p_IfS(p):
    '''IfS : IF LEFT_PAREN E RIGHT_PAREN B
           | IF LEFT_PAREN E RIGHT_PAREN B ELSE B'''

def p_WS(p):
    'WS : WHILE LEFT_PAREN E RIGHT_PAREN B'

def p_FS(p):
    'FS : FOR IDENTIFIER IN IDENTIFIER LEFT_BRACKET SL RIGHT_BRACKET'

def p_RS(p):
    'RS : RETURN E SEMICOLON'

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

parser = yacc.yacc()

# Ahora puedes utilizar el parser para analizar tu entrada
entrada = "x: int = 5;"
resultado = parser.parse(entrada, lexer=analizador)
print(resultado)
print(variables)
