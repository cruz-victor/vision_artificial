#MRO=Metodo de resolucion de orden
class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(A):
    pass
    # def hablar(self):
    #     print("Hola desde C")
        
class D(B, C):
    pass
    # def hablar(self):
    #     print("Hola desde D")
        
#Instancia de la clase D        
d=D()
#Llamar metodo hablar de la clase D
d.hablar()        
#Llamar metodo hablar de la clase especifica A
A.hablar(d)
