#Verificar la instalacion de pip: >py -m pip
#Instalar pandas: >py -m pip install pandas
#Dataframe es una estructura de datos similar a una hoja de calculo
import pandas as pd

print(type(pd))
df=pd.read_csv("archivos_csv\\datos.csv", names=["name","lastname","age"])
# print(type(df))
# print(df)
# print(df["name"])
print("Mostrar datos con slicing [:]-----------")
cadena="0123456789"
#mostrar subcadenas con slicing
# print(cadena[:])
# print(cadena[:3])
# print(cadena[2:5])
print("Ordenar df.sort_values(x)-----------")
# df_ordenado=df.sort_values("age")
# print(df_ordenado)
print("Ordenar descendentemente df.sort_values(x, ascending=False)-----------")
# df_ordenado_descendente=df.sort_values("age", ascending=False)
# print(df_ordenado_descendente)
print("Concaternar df.concta([df1,df2,df3])-----------")
# df_concatenado=pd.concat([df_ordenado, df_ordenado_descendente])
# print(df_concatenado)
print("Primeras filas df.head(x)-----------")
# primer_fila=df.head(2)
# print(primer_fila)
print("Ultimas filas df.tail(x)-----------")
# ultima_fila=df.tail(2)
# print(ultima_fila)
print("Total de filas y columnas df.shape-----------")
# filas_y_columnas_totales=df.shape
# print(filas_y_columnas_totales)
# filas, columnas=df.shape
# print(filas)
# print(columnas)
print("Informacion estadistica df.describe()-----------")
# df_info=df.describe()
# print(df_info)
print("Elemento especifico con loc df.loc[index, field]-----------")
# elemento_especifico_loc=df.loc[2,"age"]
# print(elemento_especifico_loc)
print("Elemento especifico con iloc df.iloc[a,b]-----------")
# elemento_especifico_iloc=df.iloc[2,2]
# print(elemento_especifico_iloc)
print("Todas las filas y una columna con iloc  df.iloc[n,:]-----------")
# apellidos=df.iloc[:,1]
# print(apellidos)
print("Toda una fila con todas sus columnas loc df.loc[n,:]-----------")
# fila_3=df.loc[2,:]
# print(fila_3)
print("Toda una fila con todas sus columnas iloc df.iloc[n,:]-----------")
# fila_3=df.iloc[2,:]
# print(fila_3)
print("Filtrar filas con loc  df.loc[df[field]>n,:]-----------")
mayor_que_30=df.loc[df["age"]<30,:]
print(mayor_que_30)