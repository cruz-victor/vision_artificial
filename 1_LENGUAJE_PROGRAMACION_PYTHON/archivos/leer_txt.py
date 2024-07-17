#Un archivo es un contenedor de informacion
#Un archivo tiene una extension (png, wab, doc, etc)
#Cuando un archivo se lee, cerrar para volver a leer
#Una vez cerrado el archivo, volver a usar open()

archivo_sin_leer = open("archivos\\archivo.txt", encoding="UTF-8")
# archivo=archivo_sin_leer.read()
# print(archivo)
# print("-----------")
# linea_1=archivo_sin_leer.readlines()
# print(linea_1)
# print("-----------")
# lineas=archivo_sin_leer.readlines()
# print(lineas)

# linea_1=archivo_sin_leer.readline(10)
linea_1=archivo_sin_leer.readline()
print(linea_1)

archivo_sin_leer.close()