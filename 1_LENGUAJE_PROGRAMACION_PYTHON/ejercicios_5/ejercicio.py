class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
class Estudiante(Persona):        
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

print("#---------------MAIN---------------")
estudiante=Estudiante("Victor","30","10mo")        
estudiante.mostrar_datos()
estudiante.mostrar_grado()