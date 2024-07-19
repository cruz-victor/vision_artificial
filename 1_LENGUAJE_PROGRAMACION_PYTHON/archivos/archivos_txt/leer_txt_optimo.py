#Por defecto se habre como lectura
#No es necesario cerrar el archivo
with open("archivos\\archivo_optimo.txt", encoding="UTF-8") as archivo:
    contenido=archivo.read()
    print(contenido)
    