import pandas as pd
#Leer archivo csv
df=pd.read_csv("ejercicios_3\\datos.csv")

print("------------------------------------------------")
#Convertir la columna df["edad"] a string
# df["edad"]=df["edad"].astype(str)
# print(type(df["edad"]))

print("------------------------------------------------")
#Mostrar el tipo de la columna ["edad"], fila 0
print(type(df["edad"][0]))

print("------------------------------------------------")
#Remplazar en la columna apellido el apellido "Cruz"
# df["apellido"].replace("Cruz", "CruzRemplazodo", inplace=True)

print("------------------------------------------------")
#Eliminar las filas con datos vacios NaN
print(df)
print("Eliminar los datos faltantes NaN")
df=df.dropna()
print(df)
print("Eliminar filas repetidas")
#Eliminar las filas duplicadas
df=df.drop_duplicates()
print(df)
print("------------------------------------------------")
#Crear csv con el df resultadnte
df.to_csv("ejercicios_3\\datos_limpios.csv")