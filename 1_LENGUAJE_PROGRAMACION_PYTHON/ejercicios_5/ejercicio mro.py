class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
        
class Murcielado(Mamifero, Ave):
    pass

print("#--------------------MAIN--------------------")
murcielado=Murcielado()
murcielado.comer()
murcielado.volar()
murcielado.amamantar()

print("#-----------------")
pato=Ave()
pato.comer()
pato.volar()
#pato.amamantar() #No es posible, el pato no amamanta