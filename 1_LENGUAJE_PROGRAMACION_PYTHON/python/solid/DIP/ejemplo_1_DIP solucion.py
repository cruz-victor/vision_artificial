from abc import ABC, abstractmethod


class Motor(ABC):
    @abstractmethod    
    def arrancar(self):pass

class Motor_Toyota(Motor):
    def arrancar(self):
        print("Motor de Toyota arrancado...")

class Motor_BMW(Motor):
    def arrancar(self):
        print("Motor de BMW arrancado...")        
        
class Coche:
    def __init__(self, Motor):
        self.__Motor=Motor
        
    def encender(self):
        self.__Motor.arrancar()        
        
#-----MAIN-------
motor_toyota=Motor_Toyota()
auto_toyota=Coche(motor_toyota)        
auto_toyota.encender()
print("Despues de cambiar el motor---")
motor_bmw=Motor_BMW()
auto_toyota=Coche(motor_bmw)        
auto_toyota.encender()