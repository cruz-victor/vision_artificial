#Clase absracta
#Es como una plantilla que a partir del cual se crear comportamientos
#Es un tipo de receta
#Fomenta el polimorfismo, todos pueden usar los mismos metodos

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad
        
    @abstractclassmethod    
    def hacer_actividad(self):
        pass
    
    @abstractclassmethod
    def presentarse(self):
        pass



class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
       
    def presentarse(self):
        print("Hola soy estudiante.")     
    

        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")        
        
    def presentarse(self):
        print("Hola soy trabajador.")

print("--------------MAIN------------")
victor = Estudiante("Victor",25,"Masculino","Programacion")
victor.presentarse()
victor.hacer_actividad()

pedro = Trabajador("Pedro",20,"Masculino","Albanil")
pedro.presentarse()
pedro.hacer_actividad()