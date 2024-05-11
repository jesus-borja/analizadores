
Ejemplo del lenguaje:

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

- puede tener números pero debe empezar con una letra
- letras
- guiones bajos

# Palabras Clave

- fun 
- ->
- return
- if
- else
- for 
- in 
- while
- true
- false

# Operadores asignacion

- id : tipo = valor
- id := valor
- id : tipo

# Operadores Aritméticos

- +
- -
- *
- /
- %
- //
- **

# Operadores Lógicos

- =
- <
- >
- <=
- >=
- !=
- !
- &&
- ||

# Comentarios

- /? comentario de bloque ?/

# Tablas de Tokens


| Componente Léxico        | Lexema                             | Expresión Regular           | 
| ------------------------ | ---------------------------------- | --------------------------- | 
| fun                      | fun                                | fun                         | 
| ->                       | ->                                 | ->                          | 
| if                       | if                                 | if                          | 
| else                     | else                               | else                        | 
| Operadores Aritméticos   | +, -, *, /, //, **, %              | "(+\| -\|*\|/\| //  \| **)" | 
| Operadores de Asignación | :, :=                              | (:\| :=)                    | 
| Operadores Lógicos       | =, <, >, >=, <=, !=, !, &&, "\|\|" | (=\|<\| > \| <= \| >= \| != \| ! \| && \| "\|\|")                 | 
| Cadenas de texto         | "any"                              | (\"[^\s\"]\")               | 
| Números Literales        | 0-9                               | \d+                         | 
| for                      | for                                | for                         | 
| in                       | in                                 | in                          | 
| while                    | while                              | while                       | 
| true                     | true                               | true                        | 
| false                    | false                              | false                       | 
| Identificador            | _abcd123                           | [(\w+\d?)^+]                | 
