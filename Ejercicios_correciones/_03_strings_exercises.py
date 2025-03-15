# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
from itertools import count


python = "Aprendiendo Python"
print(len(python))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola" + " " + "python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
cadena ="esto es una cadena \n con salto de linea"
print(cadena)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname , age = "David", "fernandez", 33
print(f"Mi nombre es {name}, mi apellido es {surname} y mi edad es {age}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
word = "Python"
a,b,c,d,e,f =word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
word = "Programcion"
slice_word = word[3:8]
print(word) 

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
word = "Python"
slice_word = word[::-1]
print(slice_word)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
python = "Aprendiendo Python"
capitalize_python = python.upper()
print(capitalize_python)

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
word = "Programacion en python"
print(word.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
cadena = "12345"
print(cadena.isnumeric()) 

