from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def comer(self):
        pass
    @abstractmethod
    def trabajar(self):
        pass
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador):    
    def comer(self):
        print("El humano esta comiendo.")
    
    def trabajar(self):
        print("El humano esta trabajando.")
    
    def dormir(self):
        print("El humano esta durmiendo.")

class Robot(Trabajador):
    def comer(self):
        print("El robot esta comiendo. (ERROR)")
    
    def trabajar(self):
        print("El robot esta trabajando.")
    
    def dormir(self):
        print("El robot esta durmiendo. (ERROR)")
        
#------------MAIN------------
victor = Humano()
victor.comer()
victor.trabajar()
victor.dormir()       

elon=Robot()
elon.comer()
elon.trabajar()
elon.dormir()