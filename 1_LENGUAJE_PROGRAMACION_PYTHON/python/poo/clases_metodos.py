class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
        
    def llamar(self):
        print(f"Llamando desde el celular {self.marca}")
        
    def cortar(self):
        print(f"Cortando desde el celular {self.marca}")
        

celular_samsung=Celular("Samsung","S23","48Mpx")
celular_samsung.llamar()
celular_samsung.cortar()