#Funcion para obtener el asistente y el profesor segun la edad
def get_colleagues(number_of_colleagues):
    #Crear una lista para guardar los companeros
    colleagues=[]
    #Ejecutar para pedir informacion de cada companero
    for _ in range(number_of_colleagues):
        name= input("Ingrese el nombre del compañero: ")
        age= int(input("Ingrese la edad del compañero: "))
        colleague=(name, age)
        
        #Agregar la informacion (tupla) a la lista
        colleagues.append(colleague)
    
    #Ordenar de menor a mayor las informacion de los companeros (tupla) en la lista
    colleagues.sort(key=lambda x:x[1])

    #Obtener de la lista al asistente y al profesor
    #La lista contiene tuplas. Varias [filas][columna(0)=nombre, columna(1)=edad]
    assistant=colleagues[0][0]
    teacher=colleagues[-1][0]

    return assistant, teacher

assistant, teacher = get_colleagues(5)
print(f"El profesor es: {teacher} y su asistente es {assistant}")