# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
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
