class Celular():        
    #Constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo=modelo
        self.camara=camara
    
celular_samsung=Celular("Samsung","S23","48Mpx")
celular_apple=Celular("Apple","A15","24Mpx")
print(celular_samsung.marca)
print(celular_apple.marca)