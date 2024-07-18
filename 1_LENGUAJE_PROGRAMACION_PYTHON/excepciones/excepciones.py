def sumar_dos_numeros():
    while True:
        numero_1=input("Numero 1: ")
        numero_2=input("Numero 2: ")
        try:
            resultado=int(numero_1)+int(numero_2)
            break
        except ValueError as v:
            print("Excepcion: error de valor")
        except ZeroDivisionError as d:
            print("Excepcion: division entre cero")    
        except Exception as e:
            print("Te pedi un numero tonto. ")
            print(f"Excepcion general: {e}")        
        finally:
            print("El finally se ejecuta siempre")   
    return resultado

print(sumar_dos_numeros()) 
