class Motor:
    def arrancar(self):
        print("Motor arrancado")
        
class Coche:
    def __init__(self, Motor):
        self.__Motor=Motor
        
    def encender(self):
        self.__Motor.arrancar()        