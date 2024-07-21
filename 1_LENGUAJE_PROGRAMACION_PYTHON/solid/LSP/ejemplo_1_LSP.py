#Clase abstracta
class Abstract_Sale: #T
    def __init__(self, amount, customer, taxes):
        self.__amount=amount
        self.__customer=customer
        self.__taxes=taxes
        
    def generate(self): pass
    def calculate_taxes(self):pass
    
    
class Sale(Abstract_Sale):
    def __init__(self, amount, customer, taxes):
        self.__amount=amount
        self.__customer=customer
        self.__taxes=taxes
        
    def generate(self):
        print("Se genera la venta")
    
    #En ventas al extrajero no hay impuestos    
    #No cumple con LSP
    def calculate_taxes(self):
       raise NotImplementedError


class Foreign_Sale(Abstract_Sale):
    def __init__(self, amount, customer, taxes):
        self.__amount=amount
        self.__customer=customer
        self.__taxes=taxes
        
    def generate(self):
        print("Se genera la venta")
        
    def calculate_taxes(self):
        print("Se calculan los impuestos")    

#-----------MAIN------------
sale=Abstract_Sale()
sale=Sale()
sale.calculate_taxes()
sale.generate()