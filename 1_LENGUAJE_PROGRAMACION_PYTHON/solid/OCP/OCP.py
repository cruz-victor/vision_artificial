#OCP - Open Close Principle
#Abiertas para la extension y cerradas para la modificacion
#Agregar nuevas funcionalidad sin cambiar el codigo
#Crear una clase que implement todo lo importante, las particularidades tiene que implementar la clase
#Para lograr OCP se definen contratos mediante interfaces o clases abstractas, principalmente
#Metodos para lograr OCP:
    #Interfaces y clases abstractas
    #Herencia y sobreescritura
#Proceso
    #Interface
        #Definir el metodo principal y parametros en la interface 
    #Clases con Interfaces
        #Implementar la interface para la diferentes extensiones
    #Clase Principal
        #Crear una clase
        #Inyectar la interface
        #Crear un metodo que invoque al metodo de la interface
#Analogia:
    #Enchufes y adaptadores
        #Enchufe de pared y deferentes tipos de dispositivos electricos
        #Enchufe de pared, esta cerrado para modificaciones, tiene un contrato enchufe        

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Email a {self.usuario} ")
        
class NotificadorSms(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario} ")        
        
class NotificadorWhattsap(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Whattsap a {self.usuario} ")                