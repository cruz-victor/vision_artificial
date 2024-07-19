class Persona:
    def __init__(self, nombre, edad):
        self.__nombre=nombre
        self.__edad=edad
        
    
    # def get_nombre(self):
    #     return self.__nombre
        
    # def set_nombre(self, nuevo_nombre):
    #     self.__nombre=nuevo_nombre
    
    @property
    def nombre(self):
        return self.__nombre
        
    @nombre.setter    
    def nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre    

        
print("---------MAIN---------")
print("Mostrar nombre:")
victor=Persona("victor",20)
# print(victor.get_nombre())
# print(victor.get_nombre())
print(victor.nombre)
print("Cambiar nombre:")
# victor.set_nombre("Victor Manuel")
# print(victor.get_nombre())
victor.nombre="Juan Manuel"
print(victor.nombre)