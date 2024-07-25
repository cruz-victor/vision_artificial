#SRP, Principio de respnsabidad unica
    #Una clase tiene que tener una unica responsabilidad    
    #Una unica responsabilidad = Un solo proposito = Un rol unico 
    #Es una forma de modularizar
    #Una unica responsabilidad no significa tener un solo metodo
    #Una clase puede tener varios metodos que esten relacionado a un unica responsabilidad
    #Analogia:
        #Recursos Humanos, tiene una unica responsabilidad, gestionar las contrataciones de empleados
        #Contabilidad, tiene una unica responsabilidad, manejar las finanzas
        #Sistemas, tiene una unica responsablidad, gestionar la infraestructura tecnologica
            #Si un departamente intentara asumir las responsabilidad de otro, se volverria ineficiente y propenso a errores
        
class Auto:
    def __init__(self, tanque):
        self.posicion=0
        self.tanque=tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible()>=distancia/2:
            self.posicion+=distancia
            self.tanque.usar_combustible(distancia/2)
            print("Has movido el auto existosamente.")
        else:
            print("No hay suficiente combustible.")
            
    def obtener_posicion(self):
        return self.posicion
    
    #Clase auto se encarga del moviento del auto como del combustible, no cumple con SRP                
    # def agregar_combustible(self, cantidad):
    #     self.combustible+=cantidad
    
    # def obtener_combustible(self):
    #     return self.combustible
                        
class TanqueDeCombustible:
    def __init__(self):
        self.combustible=100
        
    def agregar_combustible(self, cantidad):
        self.combustible+=cantidad
    
    def obtener_combustible(self):
        return self.combustible
        
    def usar_combustible(self, cantidad):
        self.combustible-=cantidad
        
#-------------MAIN----------------
tanque=TanqueDeCombustible()
auto=Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(100)