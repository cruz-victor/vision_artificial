#Principio de Susticion de Liskov
#LSP es un a extension del OCP. Mismo comportamiento con atributos adicionales (ventas locales con impuesto, ventas extranjeras sin impuestos)
#Permite sustituir una clase base por la clase hija (polimorfismo) y segregar correctamente las clases para aplicar herencia
#Un objeto que hereda de la clase base deberia poder hacer si o si todo los que hace la clase base, caso contrario no cumpliria con LSP
#Una clase hija puede sustituir al padre sin cambiar el comportamiento
#Darle mayor mantenimiento al software
#Detectar casos ejemplares de las modificaciones de las clases bases
#Checklikst para cumplir con LSP
    #Las subclases pueden sustituir a la clase base 
    #No violacion de contrato, Las subclases no deben alterar el comportamiento de los metodos del contrato
    #Las subclases deben implementar todo los metodos del contrato y usarla, en caso de no usar almenos un metodo viola el principio
#Implementacion
    #Clases abstractas
    #Interfaces

class T:
    #abstract method
    def get_name(self): pass
    
class S1(T):
    def get_name(self):
        return "S1"
    
class S2(T):
    def get_name(self):
        return "S2"

#----------MAIN----------
#La clase base puede ser sustitido por una clase hija
t=T()
t=S1()
print(t.get_name())

t=S2()
print(t.get_name())
