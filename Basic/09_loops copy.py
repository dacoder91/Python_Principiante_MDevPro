# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional, pero se puede poner un else dentro de un while
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else: #tambien es opcional, se puede poner al acabar el bucle
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # con esto vuelve al for si hacer lo que hay seguido(print("Se ejecuta"))
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")



#Range()  #range(inicio, fin, salto)
# La función range() se utiliza como lista de números. Por defecto comienza desde 0 y el incremento es 1. el fin es el num -1 
# La secuencia de rango necesita al menos 1 argumento (fin). Creación de secuencias usando rango
# el range() se puede convertir en list.

print(list(range(5, 20, 2)))

for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

for i in range (5, 0, -1): # inverso
    print(i) #5,4,3,2,1