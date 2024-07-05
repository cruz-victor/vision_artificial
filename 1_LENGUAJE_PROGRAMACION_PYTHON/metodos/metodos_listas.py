#crear una lista
word_list=list(["hola","victor",34])

#obtener total de elementos de la lista
total_elements=len(word_list)

#Agregar un elemento al final de la lista
word_list.append("Gomez")

#Inserta un elemento en un posicion
word_list.insert(2, "Yacuiba")

#Extiende la lista 
word_list.extend([False,200])

#Elimina un elemento por indice
word_list.pop(0)

#Elimina un elemento partinedo del final por indice
word_list.pop(-1)

#Elimina un elemnento por su valor 
word_list.remove("Yacuiba")

#Limpia toda la lista
#word_list.clear()

#Buscar elemento x en la lista
element_index_search=word_list.index("victor")

print(element_index_search)
print(word_list)


number_list=([50,10,30,100])

#Ordenar la lista ascendentemente
number_list.sort()

#Ordenar la lista descendente
# number_list.sort(reverse=True)
number_list.reverse()

print(number_list)
