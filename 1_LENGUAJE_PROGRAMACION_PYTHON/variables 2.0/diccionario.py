# dictionary=dict(name="victor", last_name="cruz")
# print(dictionary)

#Las tuplas pueden ser claves
dictionary_one={("juan", "quintanilla"):"jaja"}
print(dictionary_one)

#Las listas no pueden ser claves porque son mutables o unhasheable
# dictionary_two={["juan", "quintanilla"]:"jaja"}
# print(dictionary_two)

#Las conjunto no pueden ser claves porque son mutables o unhasheable
# dictionary_three={{"juan", "quintanilla"} :"jaja"}
# print(dictionary_three)

#Creando diccionario con fromkeys
dictionary_four=dict.fromkeys(["name","last_name"])
print(dictionary_four)
print(dictionary_four['name'])

dictionary_five=dict.fromkeys("abcde","data")
print(dictionary_five)
