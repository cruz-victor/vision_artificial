#Clase abstracta
class Abstract_Sale:
    def __init__(self, amount, customer, taxes):
        self.__amount=amount
        self.__customer=customer        
        
    def generate(self): pass    

#Clase abstracta
class Abstract_Sale_With_Taxes(Abstract_Sale):
    def __init__(self, taxes):
        self.__taxes=taxes
        
    def calculate_taxes(self): pass
      
    
class Local_Sale(Abstract_Sale_With_Taxes):
    def __init__(self, amount, customer, taxes):
        self.__amount=amount
        self.__customer=customer
        self.__taxes=taxes
        
    def generate(self):
        print("Se genera la venta")
    
    def calculate_taxes(self):
       print("Calcular impuetos")


class Foreign_Sale(Abstract_Sale):
    def __init__(self, amount, customer):
        self.__amount=amount
        self.__customer=customer
        
    def generate(self):
        print("Se genera la venta")
        

#-----------MAIN------------
sale_with_taxes=Local_Sale(100, "Juan", 0.15)
sale_with_taxes.calculate_taxes()
sale_with_taxes.generate()

sale_foreing=Foreign_Sale(200, "Pedro")
sale_foreing.generate()