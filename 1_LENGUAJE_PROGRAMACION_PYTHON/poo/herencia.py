class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        
    def hablar(self):        
        print("Hola, estoy hablando un poco...")
    
        
class Empleado(Persona):
    #pass
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, nota, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.nota=nota
        self.universidad=universidad

victor=Empleado("Victor", 39, "Boliviano","Programador",100)
print(victor.nombre)
print(victor.edad)
print(victor.nacionalidad)
print(victor.trabajo)
print(victor.nacionalidad)
victor.hablar()

print("------------------------------------------------")

juan=Estudiante("Juan", 40, "Boliviano","Informatica","UMSA")
print(juan.nombre)
juan.hablar()