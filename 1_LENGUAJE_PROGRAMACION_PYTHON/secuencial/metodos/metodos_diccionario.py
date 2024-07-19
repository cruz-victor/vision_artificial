#Crear un diccionario
dictionary={
    "nombre":"victor",
    "apellido":"cruz",
    "suscriptores":1000
}

#Obtener todos los keys del diccionario
keys=dictionary.keys()

#Obtener un elemento con get. get no lanza excepcion
name=dictionary.get("nombre")

#Eliminar todos los elementos del diccionario
# dictionary.clear()

#Eliminar un elemento del diccionario
dictionary.pop("apellido")

#Obtener los elementos del diccionario
dictionary_iterable=dictionary.items()

print(keys)
print(name)
print(dictionary)
print(dictionary_iterable)