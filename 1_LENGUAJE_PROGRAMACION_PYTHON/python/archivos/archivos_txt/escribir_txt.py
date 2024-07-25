#w=sobreescribe el archivo
#a=agregar en el archivo
with open("archivos\\archivo_escribir.txt","w", encoding="UTF-8") as archivo:
    # archivo.write("Hola vic desde consola")
    archivo.writelines(["Hola maestro como andas", " misericordia "," Juan Quintanilla\n"])
    archivo.writelines(["Hola maestro como andas2", " misericordia2 "," Juan Quintanilla2\n"])