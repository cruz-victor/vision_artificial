#Decoradores
#Es una funcion especial que decora a otra funcion
#Agrega un codigo extra antes o despues a una funcion que es pasado como parametro a otra funcion
#Una funcion dentro de otra funcion

def deco(funcion):
    def funcion_modificada():
        print("Antes de llamar a l a funcion modificada...")
        funcion()
        print("Despues de llamar a l a funcion modificada...")
    return funcion_modificada
        
print("--------------MAIN--------------")
print("-----Primera forma de llamar a una decorador") 
def saludo():
    print("Hola victor")
    
saludo_modificado=deco(saludo)
saludo_modificado()

print("-----Segunda forma de llamar a una decorador")
@deco
def saludo():
    print("Hola victor")
saludo()    