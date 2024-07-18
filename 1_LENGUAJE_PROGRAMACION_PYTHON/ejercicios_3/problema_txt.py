nombres=["Juan","Maria","Pedro"]
apellidos=["Perez","Gomez","Sanchez"]

with open("ejercicios_3\\archivo_nombres_apellidos.txt","w") as archivo:
    for nombre, apellido in zip(nombres, apellidos):
        archivo.write(f"Nombre: {nombre}\n Apellido: {apellido} \n-----------\n")    