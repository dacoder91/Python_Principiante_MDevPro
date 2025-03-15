# 1. Declara y asigna valores a las siguientes variables:
# •	name: una cadena que contenga tu nombre.
# •	age: un número entero que represente tu edad.
# •	height: un número flotante que represente tu altura.
# •	Imprime cada variable en una línea separada.

name = "David"
age = 33
height = 1.68

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
print ("tengo " + str(age) + " años")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print(is_student)
# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
complete_name = "David Fernandez Nadales"
print(len(complete_name))
# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, last_name1, last_name2 = "david", "fernandez", "nadales"
print(name + " " + last_name1 + " " + last_name2)
# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
# colour = input("Wich is your favourite colour?")
# print(colour)
# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Banana"
print(fruit)
fruit = "Pear"
print(fruit)
# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 10.5
price = int(price)
print(price)
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección 
# usando la función len(). Imprime el resultado.
adress_len = len("Calle falsa")
print(adress_len)
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. 
# Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().

phone: int = 123456789
print(type(phone))
phone = 987654321
print(type(phone))

