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

# Operadores asignacion

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

| Tipo                           | Token         | Lexema | Función                             |
| ------------------------------ | ------------- | ------ | ----------------------------------- |
|                                | IDENTIFIER    |        | Identificador                       |
| Operadores matemáticos         | PLUS          | +      | Operador de suma                    |
|                                | MINUS         | -      | Operador de resta                   |
|                                | TIMES         | \*     | Operador de multiplicación          |
|                                | DIVIDE        | /      | Operador de división                |
|                                | MODULO        | %      | Operador de módulo                  |
|                                | POWER         | \*\*   | Operador de potencia                |
|                                | ASSIGN_OP     | :=     | Operador de asignación              |
| Operadores logicos             | COMPARISON    | =      | Operador de comparación             |
|                                | LESS_THAN     | <      | Operador menor que                  |
|                                | GREATER_THAN  | >      | Operador mayor que                  |
|                                | GREATER_EQUAL | >=     | Operador mayor o igual que          |
|                                | LESS_EQUAL    | <=     | Operador menor o igual que          |
|                                | NOT_EQUAL     | !=     | Operador de desigualdad             |
|                                | NOT           | !      | Operador de negación                |
|                                | AND           | &&     | Operador lógico AND                 |
|                                | OR            | \|\|   | Operador lógico OR                  |
| Inicio de comentario de bloque | COMMENT_START | \/?    | Inicio de comentario                |
| Fin de comentario de bloque    | COMMENT_END   | ?\/    | Fin de comentario                   |
| Paréntesis                     | LEFT_PAREN    | (      | Paréntesis izquierdo                |
|                                | RIGHT_PAREN   | )      | Paréntesis derecho                  |
| Corchetes                      | LEFT_BRACKET  | [      | Corchete izquierdo                  |
|                                | RIGHT_BRACKET | ]      | Corchete derecho                    |
| Llaves                         | LEFT_BRACE    | {      | Llave izquierda (llave de apertura) |
|                                | RIGHT_BRACE   | }      | Llave derecha (llave de cierre)     |
|                                | SEMICOLO      | ;      | Fin de instruccion                  |

# Palabras reservadas

| Tipo                   | Token    | Lexema | Función                      |
| ---------------------- | -------- | ------ | ---------------------------- |
| Funcion                | FUNCTION | fun    | Define una función           |
|                        | RETURNS  | return | Indica un retorno            |
| Estructuras de control | IF       | if     | Estructura de control 'if'   |
|                        | ELSE     | else   | Estructura de control 'else' |
|                        | FOR      | for    | Bucle 'for'                  |
|                        | IN       | in     | Operador de pertenencia      |
|                        | WHILE    | while  | Bucle 'while'                |

# Tipos de datos

| Tipos de datos | Token        | Lexema | Función                   |
| -------------- | ------------ | ------ | ------------------------- |
| Tipos          | TYPE_INTEGER | int    | Valores enteros           |
|                | TYPE_STRING  | str    | Valores de texto          |
|                | TYPE_FLOAT   | float  | Valores decimales simples |
|                | TYPE_DOUBLE  | double | Valores decimales         |
|                | TYPE_BOOL    | bool   | Valores boleanos          |

# Literales de tipos de datos

| Literales | Token  | Lexema      | Función                             |
| --------- | ------ | ----------- | ----------------------------------- |
|           | STRING | "any"       | Literal de texto                    |
|           | INT    | 0-9         | Número literal                      |
|           | FLOAT  | 0-9.0-9f    | Literal número coma flotante simple |
|           | DOUBLE | 0-9.0-9     | Literal número coma flotante doble  |
|           | BOOL   | true\|false | Literal de valor boleano            |
