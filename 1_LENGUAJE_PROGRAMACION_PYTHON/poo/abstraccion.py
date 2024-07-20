#Abstraccion
#Crear una interface simple que oculte la complejidad
#La encapsulacion es parte de la abstraccion
#La abstraccion oculta la complejidad interna del sistema
#Ejemplo: Para encender un celular solo hay un boton, oculta la complejidad electronica para encender el dispositivo
class Automovil:
    def __init__(self):
        self.__estado="apagado"
        
    def encender(self):
        self.__estado="encendido"
        print("El auto esta encendido")
    
    def conducir(self):
        if self.__estado=="apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto=Automovil()
mi_auto.conducir() 