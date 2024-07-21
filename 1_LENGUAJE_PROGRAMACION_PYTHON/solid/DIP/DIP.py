#DIP
#Los modulos de alto nivel no deben depender de los modulos de bajo nivel, deben depender de abstracciones
#Las abstracciones no dependen de los detalles sino de las abstracciones
#Lo importante es depender e inyectar interfaces/clases abstractas por el contructor
#Con DIP se cumple OCP, LSP, ISP
#Usar DIP cuando se requira componer una clase con otras clases. O simular el cambio de un componente mediante constructor

#Sin DIP
# #Modulo de bajo nivel (lo menos importante)
# class Diccionario:
#     def verificar_palabras(self, palabra):
#         #Logica para verificar palabras
#         pass
    
# #Modulo de alto nivel (lo mas importante)
# class Corrector_Ortografico:
#     def __init__(self):
#         self.diccionario=Diccionario()
        
#     def corregir_texto(self,texto):
#         #Usamos el diccionario para corregir el texto
#         self.diccionario.verificar_palabras(texto)
        
        
#Con DIP
from abc import ABC, abstractmethod


class Verificador_Ortografico(ABC):
    @abstractmethod
    def verificar_palabras(self, palabra):
        pass

class Diccionario(Verificador_Ortografico):
    def verificar_palabras(self, palabra):
        #Logica para verificar palabras
        pass
    
class Diccionario_Online(Verificador_Ortografico):
    def verificar_palabras(self, palabra):
        #Logica para verificar palabras
        pass    
    
class Corrector_Ortografico:
    def __init__(self, VerificadorOrgrafico):
        self.__VerificadorOrtografico=Verificador_Ortografico
        
    def corregir_texto(self,texto):
        self.__VerificadorOrtografico.verificar_palabras(texto)        
        
#----------MAIN---------------
#Dependen de una interface no de una implementacion especifica
corrector=Corrector_Ortografico(Diccionario())
corrector=Corrector_Ortografico(Diccionario_Online())








