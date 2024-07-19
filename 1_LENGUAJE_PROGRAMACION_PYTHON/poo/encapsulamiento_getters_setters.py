#Los getters y setters encapsulan los atributos de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre=nombre
        self.__edad=edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre=new_nombre

print("----------------MAIN----------------")        
victor=Persona("Victor",21)

nombre=victor.get_nombre()
print(nombre)

victor.set_nombre("Victor Manuel")
nombre=victor.get_nombre()
print(nombre)