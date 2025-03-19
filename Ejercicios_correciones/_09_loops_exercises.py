# 1. Usa un bucle while para imprimir los números del 1 al 10.
my_num = 0
while my_num <= 10:
    print(my_num)
    my_num += 1
else: print("Finalizado")

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_list = [10, 20, 30, 40, 50]
for num in my_list:
    print(num)
else: print("Finalizado")

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
i = 1
sum = 0
while i <= 100:
    sum += i
    i +=1
print(sum)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
my_str = "Python"
for letter in my_str:
    print(letter) 
else: print("Finalizado")

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
my_num = 1
while my_num <= 50:
    if my_num / 7 == 1:
        print(f"{my_num} es divisible por 7")
        break
    my_num += 1
# v2
i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
        break
    i += 1
    

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in my_dict:
    print(key)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
else: print("Finalizado")

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for num in range(10,0,-1):
    print(num)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
my_list = [30, 10, 30, 20, 30, 40]
cont = 0
for num in my_list:
    if num == 30:
        cont += 1
print(f"hay {cont} treintas")

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
my_list = ["Paco", "Pepe", "Brais","David"]
for element in my_list:
    if element == "Brais":
        print("Brais encontrado, se acaba el bucle")
        break
    print(element)
