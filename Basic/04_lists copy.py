# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17] # pueden haber repetidos en las list 

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"] #puede tener diferentes tipos de datos

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # en Python la ultima posicion del list tambien se puede indicar con -1, no 0
print(my_other_list[-4])
print(my_list.count(30)) # indica cuantas veces hay un 30 en la lista de arriba 
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais")) #indica la en la lista del valor indicado

age, height, name, surname = my_other_list # podemos cada valor de la list, asignarlo a una variable de esta manera
#age, height, name = my_other_list #Error, pero hay que asignarle todos, no se puede solo algunos 
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list) #se pueden sumar las listas
my_list.extend(my_other_list) #tambien se puede asi
#print(my_list - my_other_list) no se puede

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev") #append para añadir un nuevo valor al finak
print(my_other_list)

my_other_list.insert(1, "Rojo") #insertamos en la posicion X el nuevo valor indicado, pero el antiguo elemento se "corre" un valor a la derecha
print(my_other_list)

my_other_list[1] = "Azul" #otra manera de hacer lo de arriba
print(my_other_list)

my_other_list.remove("Azul") #para eliminar un valor indicando su valor
print(my_other_list)

#my_other_list.remove[0] nose puede asi, eso seria con el pop

my_list.remove(30) #como tiene dos 30, elimina el primero que encuentra
print(my_list)

print(my_list.pop()) #pop elimina el ultimo elemento de la lista, si imprimes el pop() te idnciara el elemento que esta eliminanado
print(my_list)

my_pop_element = my_list.pop(2) #desapila el elemento en la posicion [2], pero mejor usar el del,
# pop es para motar o usar para algo el elementos en que hacemos pop
print(my_pop_element)
print(my_list)

del my_list[2] # elimina el valor en la posicion []
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() # copia la lista 

my_list.clear() # para vaciar la list, pero no eliminarla
print(my_list)
print(my_new_list)

my_new_list.reverse() #invierte el orden
print(my_new_list)

my_new_list.sort() # ordena la lista, se podria indicar como ordenar tambien
print(my_new_list)

my_new_list.sort(reverse=True) #tmb se puede ordenar haciendo el reverse

print(sorted(my_new_list)) #lo ordena de menor a mayor o por orden alfabetico

# Sublistas

print(my_new_list[1:3]) # imprime entre 1 y 2

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
