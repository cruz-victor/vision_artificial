import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Leer csd de pedos
df=pd.read_csv("ejercicios_3\\ingresos.csv")

#Crear grafico de barras
sns.barplot(x="fuente", y="ingresos", data=df)

plt.show()