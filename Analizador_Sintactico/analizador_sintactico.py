import ply.yacc as yacc
from analizador_lexico import tokens, analizador

variables = {}
errores_gramatica = []

# Precedencia y asociatividad de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'LESS_THAN', 'GREATER_THAN', 'LESS_EQUAL',
     'GREATER_EQUAL', 'COMPARISON', 'NOT_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('right', 'POWER'),
    ('right', 'NOT'),
)


def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]


def p_data_type(p):
    '''data_type : TYPE_INTEGER
                 | TYPE_STRING
                 | TYPE_FLOAT
                 | TYPE_DOUBLE
                 | TYPE_BOOL
                 | TYPE_VOID
                 | TYPE_NULL'''
    p[0] = p[1]


def p_factor(p):
    '''factor : LEFT_PAREN expr RIGHT_PAREN
              | IDENTIFIER
              | INT
              | FLOAT
              | DOUBLE
              | STRING
              | BOOL
              | NOT expr
              | expr COMPARISON expr
              | expr LESS_THAN expr
              | expr GREATER_THAN expr
              | expr LESS_EQUAL expr
              | expr GREATER_EQUAL expr
              | expr NOT_EQUAL expr
              | expr AND expr
              | expr OR expr'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = ('not', p[2])
    else:
        p[0] = p[1]


def p_expr(p):
    '''expr : expr PLUS factor
            | expr MINUS factor
            | expr TIMES factor
            | expr DIVIDE factor
            | expr MODULO factor
            | expr POWER factor
            | factor'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_var_decl(p):
    '''var_decl : IDENTIFIER COLON data_type ASSIGN_OP expr'''
    variables[p[1]] = p[3]
    p[0] = ('var_decl', p[1], p[3], p[5])


def p_param_list(p):
    '''param_list : param_list COMMA IDENTIFIER COLON data_type
                  | IDENTIFIER COLON data_type
                  | empty'''
    if len(p) == 6:
        p[0] = p[1] + [(p[3], p[5])]
    elif len(p) == 4:
        p[0] = [(p[1], p[3])]
    else:
        p[0] = []


def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []


def p_statement(p):
    '''statement : expr SEMICOLON
                 | return_statement SEMICOLON 
                 | var_decl SEMICOLON
                 | var_reassign SEMICOLON
                 | if_statement
                 | while_statement 
                 | for_statement
                 | func_decl
                 | block'''
    p[0] = p[1]


def p_block(p):
    '''block : LEFT_BRACE statement_list RIGHT_BRACE'''
    p[0] = p[2]


def p_if_statement(p):
    '''if_statement : IF LEFT_PAREN expr RIGHT_PAREN block
                    | IF LEFT_PAREN expr RIGHT_PAREN block ELSE block'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if_else', p[3], p[5], p[7])


def p_while_statement(p):
    '''while_statement : WHILE LEFT_PAREN expr RIGHT_PAREN block'''
    p[0] = ('while', p[3], p[5])


def p_for_statement(p):
    '''for_statement : FOR IDENTIFIER IN IDENTIFIER block'''
    p[0] = ('for', p[5])


def p_return_statement(p):
    '''return_statement : RETURN expr'''
    p[0] = ('return', p[2])


def p_func_decl(p):
    '''func_decl : FUNCTION IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW data_type block'''
    p[0] = ('function', p[2], p[4], p[7], p[8])


def p_empty(p):
    '''empty :'''
    pass


def p_var_reassign(p):
    '''var_reassign : IDENTIFIER ASSIGN_OP expr'''
    if p[1] in variables:
        variables[p[1]] = p[3]
        p[0] = ('var_reassign', p[1], p[3])
    else:
        error_message = f"Error: La variable '{p[1]}' no está declarada."
        errores_gramatica.append(error_message)
        print(error_message)


def p_error(p):
    if p:
        error_message = f"Error sintáctico en el token {p.type} ({p.value}) en la línea {p.lineno}"
        errores_gramatica.append(error_message)
        print(error_message)
    else:
        error_message = "Error sintáctico al final de la entrada"
        errores_gramatica.append(error_message)
        print(error_message)


parser = yacc.yacc()

data = """
fun factorial(x: int) -> int {
    num: int = 1;
    for i in x {
        num = num * 1;
    }
    return num;
}
"""

result = parser.parse(data)
if result:
    print("Parseo exitoso:", result)
else:
    print("Errores de gramática:", errores_gramatica)
