# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # con \ haces un salto de linea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # \t introduce una tabulacion
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" #con \\ puedes escapar el caracter
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #con .format con {}
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # con sumas y espacios es mucho peor
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #!!!!!!!!!ES LA MEJOR FORMA DE HACERLO!!!!!!!!!

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # [1:3] coge desde el 1 hasta el 3 sin incluirlo
print(language_slice)

language_slice = language[1:] # [1:] coge desde el 1 hasta el final
print(language_slice)

language_slice = language[-2] # [-2] coge el penultimo caracter de la cadena, POR DETRAS EMPIEZA EN -1
print(language_slice)

language_slice = language[0:6:2] # [0:6:2] coge desde el 0 hasta el 6 de 2 en 2
print(language_slice)

# Reverse

reversed_language = language[::-1] # [::-1] coge la cadena al reves
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) # Pone la primera letra en mayúscula   
print(language.upper()) # Pone todo en mayúsculas
print(language.count("t")) # Cuenta cuantas veces aparece la letra t
print(language.isnumeric()) # Comprueba si es un número
print("1".isnumeric()) # Comprueba si es un número
print(language.isalnum()) # Comprueba si es alfanumérico
print(language.isalpha()) # Comprueba si es alfabético
print(language.isdigit()) # Comprueba si es un número
print(language.isdecimal()) # Comprueba si es un decimal
print(language.lower()) # Pone todo en minúsculas
print(language.lower().isupper()) # Comprueba si está en mayúsculas
print(language.islower()) # Comprueba si está en minúsculas/////////
print(language.startswith("Py")) # Comprueba si empieza por Py
print("Py" == "py")  # No es lo mismo porque una empieza por mayúscula y la otra por minúscula
print(language.endswith("on")) # Comprueba si termina por on 
print(language.expandtabs(10)) # Pone un tabulador de 10 espacios
print(language.find("t")) # Busca la primera letra t, si no la encuentra devuelve -1
print(language.rfind("t")) # Busca la última letra t, si no la encuentra devuelve -1
print(language.isidentifier()) # Comprueba si es un identificador, un identificador es una variable que empieza por una letra o un guión bajo
print(language.isprintable()) # Comprueba si es imprimible
print(language.isspace()) # Comprueba si es un espacio
print(language.istitle()) # Comprueba si es un título
print(language.swapcase()) # Cambia las mayúsculas por minúsculas y viceversa
print(language.title()) # Pone la primera letra de cada palabra en mayúscula
print(language.split()) # Divide la cadena en palabras

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech) # Une los elementos de la lista con un espacio
print(result) 
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech) # Une los elementos de la lista con un #
print(result) # 'HTML# CSS# JavaScript# React'