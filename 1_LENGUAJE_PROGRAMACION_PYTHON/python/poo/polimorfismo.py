#Polimorfismo
#Mismo mensaje pero resultado diferentes
#Tipos de polimorfismo
    #Polimorfismo llamada a un metodo
    #Polimorfismo parametro de metodo

#El polimorfismo en otros lenguajes se realiza con herencia o interfaces    
#En Python no es necesario la herencia o interfaces para implementar polimorfismo
#A un animal pedirle que haga un sonido. El perro ladrara, el gato maullara, el pato cacaraqueara, etc
#Estandariaza la llamada de metodos, clases flexibles

class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
    
#Polimorfismo en metodos    
def hacer_sonido(animal):
    print(animal.sonido())
    
print("Polimorfismo llamada a metodo--------------------------------")    
gato=Gato()
print(gato.sonido())

perro=Perro()
print(perro.sonido())

print("Polimorfismo de metodo----------------------------------------")
hacer_sonido(gato)
hacer_sonido(perro)

print("Otros ejemplos de polimorfismo--------------------------------")
numero_1=10
numero_2=20.5
resultado=numero_1+numero_2
print(resultado)

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
lista_numeros=[1,2,3,4]
lista_texto="maquina"        
recorrer(lista_numeros)
recorrer(lista_texto)