Objetivo:
Desarrollar un software que implemente un análisis léxico y sintáctico básico utilizando la biblioteca PLY en Python. El software debe ser capaz de reconocer y validar expresiones en un lenguaje definido por un conjunto de reglas gramaticales. 

Instrucciones de ejecución:
El código realizado se ejecuta desde la terminal usando Python, este al momento de iniciar pedirá al usuario que ingrese una cadena de texto, en los cuales los caracteres pueden ser clasificados de distintas formas:
    • Operaciones matemáticas básicas con los operadores +, -, *, /
    • Números enteros y decimales
    • Expresiones entre paréntesis
    • Condicionales (if/else) y bucles (while)
    • Identificadores para variables (a-z,A-Z)

Una vez ingresada la cadena de texto procederá a mostrar los resultados de las clasificaciones realizadas y el proceso termina cuando se escriba salir o se cierre la terminal donde se este ejecutando el código.
Ejemplos de entrada y salida:
Entrada:
> 10 + (5 * 3)

Salida:
LexToken(NUMBER,10,1,1)
LexToken(PLUS,'+',1,4)
LexToken(LPAREN,'(',1,6)
LexToken(NUMBER,5,1,7)
LexToken(TIMES,'*',1,9)
LexToken(NUMBER,3,1,11)
LexToken(RPAREN,')',1,12)
