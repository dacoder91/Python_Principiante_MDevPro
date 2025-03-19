# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict) #es False porque busca por Key, no por el value
print("Apellido" in my_dict) #en cambio aqui será True

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) #devuelve todas las key:values
print(my_dict.keys()) #devuelve keys
print(my_dict.values()) #devuelve values

my_list = ["Nombre", 1, "Piso"]

#fromkeys 
#crea un dict sin valores , solo las claves
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev") #crea el dict con el valor "Mouredev" en todas las keys
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item