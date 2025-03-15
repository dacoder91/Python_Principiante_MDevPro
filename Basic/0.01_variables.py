# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

#Variables se escriben en minusculas y snake_case

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

#Convertir variable en otro tipo
my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)


#Len cuenta las letras
print(len(my_string_variable))

#Variables en una sola linea 
nombre, apellido, apellido2, edad = "David", "Fernandez", "Nadales", 25
print("Me llamo: ",nombre,".Y mi edad es:",edad)

# Inputs (para que el usuario escriba el valor)
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

#puedes cambiar el tipo de variable
name = 35
edad = "David"

# ¿Forzamos el tipo? No se puede, solo serviria para informar
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

