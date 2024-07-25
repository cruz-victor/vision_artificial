#Encapsulamiento
#Protege los elementos de una clase (private, public, protected)
#En python los conceptos son public, private (_) y very private (__)
#Para acceder a datos privados se usan getters y setters

class MiClase:
    def __init__(self):
        self.atributo_publico="valor public"
        self._atributo_privado="valor privado"
        self.__atributo_muy_privado="valor muy privado"
        
    def metodo_publico(self):
        print("Hola, como estas vic")
        
    def _metodo_privado(self):
        print("Hola, como estas vic privado")        
        
    def __metodo_muy_privado(self):
        print("Hola, como estas vic muy privado")                
        
print("----------------------")        
objeto=MiClase()
print(objeto.atributo_publico)
print(objeto._atributo_privado)
# print(objeto.__atributo_muy_privado)
        
        