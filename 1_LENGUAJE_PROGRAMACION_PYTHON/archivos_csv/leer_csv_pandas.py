#Verificar la instalacion de pip: >py -m pip
#Instalar pandas: >py -m pip install pandas
#Dataframe es una estructura de datos similar a una hoja de calculo
import pandas as pd

print(type(pd))
df=pd.read_csv("archivos_csv\\datos.csv", names=["name","lastname","age"])
# print(type(df))
# print(df)
# print(df["name"])
print("-----------")
cadena="0123456789"
#mostrar subcadenas con slicing
# print(cadena[:])
# print(cadena[:3])
# print(cadena[2:5])
print("-----------")
# df_ordenado=df.sort_values("age")
# print(df_ordenado)
print("-----------")
# df_ordenado_descendente=df.sort_values("age", ascending=False)
# print(df_ordenado_descendente)
print("-----------")
# df_concatenado=pd.concat([df_ordenado, df_ordenado_descendente])
# print(df_concatenado)
print("-----------")
# primer_fila=df.head(2)
# print(primer_fila)
print("-----------")
# ultima_fila=df.tail(2)
# print(ultima_fila)
print("-----------")
# filas_y_columnas_totales=df.shape
# print(filas_y_columnas_totales)
# filas, columnas=df.shape
# print(filas)
# print(columnas)
print("-----------")
# df_info=df.describe()
# print(df_info)
print("-----------")
# elemento_especifico_loc=df.loc[2,"age"]
# print(elemento_especifico_loc)
print("-----------")
# elemento_especifico_iloc=df.iloc[2,2]
# print(elemento_especifico_iloc)
print("-----------")
# apellidos=df.iloc[:,1]
# print(apellidos)
print("-----------")
# fila_3=df.loc[2,:]
# print(fila_3)
print("-----------")
# fila_3=df.iloc[2,:]
# print(fila_3)
print("-----------")
mayor_que_30=df.loc[df["age"]<30,:]
print(mayor_que_30)