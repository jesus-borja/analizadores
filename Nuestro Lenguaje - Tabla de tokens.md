# Ejemplo del lenguaje:

```
fun factorial() -> void {
	x: int = 25;
	y: float = 2.3f;
	str := "cadena";

	if (y >= x) {
		print("Hola");
		return;
	} else {
		read(x);
		print(x);
	}

	/? comentario
	de
	bloque
	?/
	xs := {21, 22, 23,}

	for _x in xs {
		print(_x)
	}
	while true {
		print("a")
	}
}
```

# Identificador

-   puede tener números pero debe empezar con una letra
-   letras
-   guiones bajos

# Palabras Clave

-   fun
-   ->
-   return
-   if
-   else
-   for
-   in
-   while
-   true
-   false

# Operadores de asignacion

-   id : tipo = valor
-   id := valor
-   id : tipo

# Operadores Aritméticos

-   \+
-   \-
-   \*
-   /
-   %
-   \*\*

# Operadores Lógicos

-   =
-   <
-   \>
-   <=
-   \>=
-   !=
-   !
-   &&
-   ||

# Comentarios

-   /? comentario de bloque ?/

# Tablas de Tokens

# Tabla de tokens

| Tipo                           | Token            | Lexema   | Función                             | Expresión Regular      |
| ------------------------------ | ---------------- | -------- | ----------------------------------- | ---------------------- |
| Identificador                  | IDENTIFIER       | abc123\_ | Identificador                       | [a-zA-Z\_][a-zA-Z0-9_] |
| Operadores matemáticos         | PLUS             | +        | Operador de suma                    | \\\+                   |
|                                | MINUS            | -        | Operador de resta                   | \\\-                   |
|                                | TIMES            | \*       | Operador de multiplicación          | \\\*                   |
|                                | DIVIDE           | /        | Operador de división                | /                      |
|                                | MODULO           | %        | Operador de módulo                  | %                      |
|                                | POWER            | \*\*     | Operador de potencia                | \*\*                   |
|                                | ASSIGN_OP        | :=       | Operador de asignación implícita    | :=                     |
|                                | TYPE_DECLARATION | :        | Operador de asignación explícita    | :                      |
| Operadores logicos             | COMPARISON       | =        | Operador de comparación             | =                      |
|                                | LESS_THAN        | <        | Operador menor que                  | <                      |
|                                | GREATER_THAN     | >        | Operador mayor que                  | >                      |
|                                | GREATER_EQUAL    | >=       | Operador mayor o igual que          | >=                     |
|                                | LESS_EQUAL       | <=       | Operador menor o igual que          | <=                     |
|                                | NOT_EQUAL        | !=       | Operador de desigualdad             | !=                     |
|                                | NOT              | !        | Operador de negación                | !                      |
|                                | AND              | &&       | Operador lógico AND                 | &&                     |
|                                | OR               | \|\|     | Operador lógico OR                  | \\\|\\\|               |
| Inicio de comentario de bloque | COMMENT_START    | \/?      | Inicio de comentario                | \/\\?                  |
| Fin de comentario de bloque    | COMMENT_END      | ?\/      | Fin de comentario                   | \\?\/                  |
| Paréntesis                     | LEFT_PAREN       | (        | Paréntesis izquierdo                | \\\(                   |
|                                | RIGHT_PAREN      | )        | Paréntesis derecho                  | \\\)                   |
| Corchetes                      | LEFT_BRACKET     | [        | Corchete izquierdo                  | \\\[                   |
|                                | RIGHT_BRACKET    | ]        | Corchete derecho                    | \\\]                   |
| Llaves                         | LEFT_BRACE       | {        | Llave izquierda (llave de apertura) | \\\{                   |
|                                | RIGHT_BRACE      | }        | Llave derecha (llave de cierre)     | \\\}                   |
|                                | SEMICOLO         | ;        | Fin de instruccion                  | ;                      |

# Palabras reservadas

| Tipo                   | Token    | Lexema | Función                      | Expresión Regular |
| ---------------------- | -------- | ------ | ---------------------------- | ----------------- |
| Funcion                | FUNCTION | fun    | Define una función           | fun               |
|                        | RETURNS  | ->     | Indica un retorno            | ->                |
| Estructuras de control | IF       | if     | Estructura de control 'if'   | if                |
|                        | ELSE     | else   | Estructura de control 'else' | else              |
|                        | FOR      | for    | Bucle 'for'                  | for               |
|                        | IN       | in     | Operador de pertenencia      | in                |
|                        | WHILE    | while  | Bucle 'while'                | while             |

# Tipos de datos

| Tipos de datos | Token        | Lexema | Función                         | Expresión Regular |
| -------------- | ------------ | ------ | ------------------------------- | ----------------- |
| Tipos          | TYPE_INTEGER | int    | Valores enteros                 | int               |
|                | TYPE_STRING  | str    | Valores de texto                | str               |
|                | TYPE_FLOAT   | float  | Valores decimales simples       | float             |
|                | TYPE_DOUBLE  | double | Valores decimales               | double            |
|                | TYPE_BOOL    | bool   | Valores boleanos                | bool              |
|                | TYPE_VOID    | void   | Indicar funciones sin retorno   | void              |
|                | TYPE_NULL    | null   | Representa la ausencia de valor | null              |

# Literales de tipos de datos

| Literales | Token  | Lexema      | Función                             | Expresión Regular |
| --------- | ------ | ----------- | ----------------------------------- | ----------------- |
|           | STRING | "any"       | Literal de texto                    | "[^\s\"]"         |
|           | INT    | 0-9         | Número literal                      | [0-9]+            |
|           | FLOAT  | 0-9.0-9f    | Literal número coma flotante simple | [0-9]+\.[0-9]+f   |
|           | DOUBLE | 0-9.0-9     | Literal número coma flotante doble  | [0-9]+\.[0-9]+    |
|           | BOOL   | true\|false | Literal de valor boleano            | (true\|false)     |
