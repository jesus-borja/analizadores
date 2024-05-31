### Introducción

En el ámbito del desarrollo de compiladores e intérpretes, el análisis sintáctico es una fase crucial que sigue al análisis léxico. Mientras que el analizador léxico se encarga de dividir el código fuente en una serie de tokens, el analizador sintáctico (o parser) toma estos tokens y los organiza en una estructura jerárquica conocida como árbol sintáctico o árbol de derivación. Esta estructura refleja la gramática del lenguaje de programación y permite identificar la correcta disposición y relación de los elementos en el código.

### ¿Para qué sirve?

El propósito principal de un analizador sintáctico es garantizar que el código fuente cumpla con las reglas sintácticas del lenguaje de programación. Es decir, verifica que la secuencia de tokens generada por el analizador léxico esté organizada de manera que se ajuste a la gramática del lenguaje. Esto incluye la detección de errores como la falta de paréntesis, la incorrecta anidación de bloques de código, la declaración y el uso inapropiado de variables, entre otros.

### ¿Cómo funciona?

Un analizador sintáctico no solo detecta y reporta errores sintácticos, sino que también facilita la generación de código intermedio, la optimización de código y la posterior generación de código máquina o bytecode. Al construir una representación estructurada del programa, el analizador sintáctico permite a las fases posteriores del compilador realizar transformaciones y optimizaciones sobre el código con mayor facilidad.

En este trabajo, se ha desarrollado un analizador sintáctico utilizando la herramienta PLY (Python Lex-Yacc), que es una implementación en Python de las conocidas herramientas lex y yacc utilizadas tradicionalmente en la construcción de compiladores. El analizador sintáctico desarrollado soporta una variedad de estructuras del lenguaje de programación, incluyendo declaraciones de variables, definiciones de funciones, condicionales y operaciones aritméticas y lógicas.

### Aplicaciones

El análisis sintáctico tiene aplicaciones en diversas áreas, tales como:

- **Compiladores e intérpretes**: Transformar código fuente en código máquina o bytecode ejecutable.
- **Edición de código**: Herramientas de desarrollo integradas (IDEs) que proporcionan resaltado de sintaxis, autocompletado y detección de errores en tiempo real.
- **Análisis estático**: Herramientas que verifican la corrección de programas sin ejecutarlos, buscando errores potenciales, malas prácticas y optimizaciones.
- **Transformación de código**: Refactorización de código y generación de documentación automatizada a partir del código fuente.

### Aclaraciones
Durante el desarrollo y las pruebas del analizador sintáctico, generamos un nuevo archivo de analizador léxico que contiene las mismas reglas pero expresadas de manera diferente. Esto nos permitió  mejorar el funcionamiento del analizador léxico para que se integrara de manera más efectiva con el analizador sintáctico.

Además, trabajamos en un entorno controlado para garantizar un mejor funcionamiento de la librería PLY y asegurar la compatibilidad y estabilidad del sistema en su conjunto. 