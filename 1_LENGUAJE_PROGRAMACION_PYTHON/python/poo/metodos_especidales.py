#Metodos especiales
#Son funciones especiales que inician con dos guiones bajos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
        
vic=Persona("Victor",25)
print(vic)