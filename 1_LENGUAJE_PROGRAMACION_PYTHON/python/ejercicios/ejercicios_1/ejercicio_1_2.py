#Leer un conjunto de palabras. Si la cantidad de caracteres del texto es mayor a 100 caracteres mostrar un mensaje que 'Es un testamento.', caso contrario mostrar que 'Es un mensaje simple.'.
# input_text="hola universo, soy victor cruz"
input_text=input("Escribe lo que estas pensando: ")
text_length=len(input_text)
print(text_length)

if text_length > 100:
    print("Es un testamento.")
else:
    print("Es un mensaje simple.")
    
    
#Leer un conjunto de palabras. Si las palabras del texto es mayor a 100 caracteres mostrar un mensaje que 'Es un testamento, hay muchas palabras.', caso contrario mostrar que 'Es un mensaje simple, hay pocas palabras.'.
words=input_text.split(" ")
number_of_words=len(words)
print(words)
print(number_of_words)
print(f"El texto contiene {number_of_words} palabras")

if number_of_words>100:
    print("Es un testamento, hay muchas palabras.")
else:
    print("Es un mensaje simple, hay pocas palabra.")
    