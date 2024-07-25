#ISP
#Principio de Segregacion de Interfaces
#Ningun Clase tiene que ser forzado a depender de interfaces que no utilicen
#Es mejor tener muchas interfaces especificas que una unica interface general. Ayuda a reducir el acoplamiento y aumentar la cohesion en el diseno del software

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    @abstractmethod
    def reportar_horas(self):
        pass
    @abstractmethod
    def obtener_salario(self):
        pass
    @abstractmethod
    def gestionar_equipo(self):
        pass
    
class Desarrollador(Empleado):    
    def trabajar(self):
        print("Trabajando...")
    
    def reportar_horas(self):
        print("Reportar horas...")        

    def obtener_salario(self):
        print("Obteniendo salario...")

    def gestionar_equipo(self):
        raise NotImplementedError("No aplica para desarrolladores")
        
#------------MAIN------------
victor = Desarrollador()
victor.trabajar()
victor.reportar_horas()
victor.obtener_salario()
# victor.gestionar_equipo()

#-----------SOLUCION CON ISP----------------
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Reportador(ABC):
    @abstractmethod
    def reportar_horas(self):
        pass
    
class Receptor_Salario(ABC):
    @abstractmethod
    def obtener_salario(self):
        pass
  
class Gestor_Equipo(ABC):
    @abstractmethod
    def gestionar_equipo(self):
        pass 
    
    
class Desarrollador_Mejorado(Trabajador, Reportador, Receptor_Salario):    
    def trabajar(self):
        print("Trabajando v2...")
    
    def reportar_horas(self):
        print("Reportar horas v2...")        

    def obtener_salario(self):
        print("Obteniendo salario v2...")
    
#------------MAIN------------        
vic=Desarrollador_Mejorado()
vic.trabajar()
vic.reportar_horas()
vic.obtener_salario()
