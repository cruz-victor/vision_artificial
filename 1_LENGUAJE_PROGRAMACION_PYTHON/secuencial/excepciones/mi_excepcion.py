class MiExcepcion(Exception):
    def __init__(self, error):
        print(f"Impresionante, cometiste el siguiente error: {error}")
        
#Manejar excepcion
try:
    raise MiExcepcion("jajajaj persona poco culta")
except:
    print("Como vas a cometer ese error")
    
#Lanzar excepcion
raise MiExcepcion("jajajaj persona poco culta")