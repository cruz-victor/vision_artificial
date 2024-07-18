def sumar_dos_numeros():
    while True:
        numero_1=input("Numero 1: ")
        numero_2=input("Numero 2: ")
        try:
            resultado=int(numero_1)+int(numero_2)
            break
        except:
            print("Te pedi un numero tonto.")   
    return resultado

print(sumar_dos_numeros()) 
