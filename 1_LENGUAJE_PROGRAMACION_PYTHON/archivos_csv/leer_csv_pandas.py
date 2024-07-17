#Verificar la instalacion de pip: >py -m pip
#Instalar pandas: >py -m pip install pandas
#Dataframe es una estructura de datos similar a una hoja de calculo
import pandas as pd

print(type(pd))
df=pd.read_csv("archivos_csv\\datos.csv", names=["name","lastname","age"])
print(type(df))
print(df)
print(df["name"])