# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
num = 5
if num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")
else:
    print("Es cero")
    
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
age = int(input("Cual es tu edad?"))
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
my_string = input("introduce una cadena")
if my_string:
    print("Mi cadena no esta vacia")
else:
    print("La cadena esta vacia")
    
if not my_string:
    print("Esta vacia")
else:
    print("No esta vacia")
    
# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
if num1 > num2:
    print(num1 + "Es mayor que: " + num2)
elif num1 < num2:
    print(num2 + "Es mayor que: " + num1)
else:
    print("Son iguales.")
#####################v2
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales.")    


# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
my_num = int(input("Introduce un numero"))
if my_num % 3 == 0 and my_num % 5 == 0:
    print(f"{my_num} es divisible por 3 y 5 a la vez")
else:
    print(f"{my_num} NO es divisible por 3 y 5 a la vez")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
my_num = int(input("Escriba un numero"))
if my_num % 2 ==0:
    print("El numero es par")
else:
    print("El numero es inpar")
    
# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, 
# indica que puede votar con permiso especial.
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Puedes votar.")
elif age == 16 or age == 17:
    print("Puedes votar con permiso especial.")
else:
    print("No puedes votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, 
# muestra un mensaje de error.
default_password = "1234"
user_password = input("Write your password: ")
if user_password != default_password:
    print("La contraseña no es correcta.")
else:
    print("La contraseña es correcta.")
# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
my_num = int(input("Escriba un numero"))
if 10 <= my_num <= 20:
    print(f"{my_num} esta entre 10 y 20.")
else:
    print(f"{my_num} NO esta entre 10 y 20.")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y 
# muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
bandera = True
while(bandera):
    color = input("Introduzca el estado del semaforo: ")
    if color == "rojo":
        print("Semaforo en rojo")
        break
    elif color == "amarillo":
        print("Semaforo en amarillo")
        break
    elif color == "verde":
        print("Semaforo en verde")
        break
    else:
        print("Debe elegir  rojo, amarillo o verde")
        
#v2

color = input("Introduce un color (rojo, amarillo, verde): ").lower()
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avanza")
else:
    print("Color no válido")

