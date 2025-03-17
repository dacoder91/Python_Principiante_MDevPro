# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario ya que se inicia igual,depende lo que contenga luego es uno u otro

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) #aqui ya es set

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada!!!!!!!

my_other_set.add("MoureDev")  # Un set no admite repetidos!!!!!

my_other_set.update(["Youtuber","Discorder"]) #se puede usar update tanto con list,tuple o otros sets

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set) #Devuelve True porque si que esta dentro del Set
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

#pop() eliminar aleatorio
removed_item = my_other_set.pop()
print(removed_item)


my_other_set.clear() #vaciar el Set
print(len(my_other_set))


del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined // la variable ya no existe

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set) #asi se jutan dos sets en 1  
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set)) #RESTA A NEW SET LO QUE HAY EN MY_SET

#interesction, encuentra elementos en ambos sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

# subset y superset
#Un conjunto A es un subconjunto de un conjunto B si todos los elementos de A están contenidos en B

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True, todos los elementos que tiene st2, estan en set1


#Un conjunto A es un superconjunto de un conjunto B si todos los elementos de B están contenidos en A
print(st1.issuperset(st2)) # True, si, todo lo que hay en set2 esta en set1 
# ***Si un conjunto no contiene todos los elementos del otro, no es un subconjunto o superconjunto.

#symmetric_difference
#devuelve los elementos de ambos sets, excepto los que estan en ambos sets, en mates (A\B) ∪ (B\A)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

#joining sets
#si dos sets no tienen los mismos elementos,son disjoints, si alguno de los elementos si esta,no es disjoints 
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
