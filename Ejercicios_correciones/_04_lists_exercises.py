# 1. Crea una lista con los números del 1 al 5 e imprímela.
my_list = [1,2,3,4,5]
print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
my_list2=[0, 20, 30, 40, 50]
print(my_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
my_list2.insert(2,15)
print(my_list2)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
my_list3 = [10, 20, 30, 30, 40, 50]
my_list3.remove(30)
print(my_list2)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
my_list = [1, 2, 3, 4, 5]
valor = my_list.pop()
print(valor)
print(my_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
my_list4 = [100, 200, 300, 400, 500]
my_list4.reverse()
print(my_list4)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
my_list = [1, 2, 3]
my_other_list = [4, 5, 6]
my_new_list = my_list + my_other_list
print(my_other_list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
my_list = [10, 20, 30, 40, 50]
my_sublist = my_list[1:3]
print(my_sublist)