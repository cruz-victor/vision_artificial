import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leer csd de pedos
df=pd.read_csv("ejercicios_3\\pedos.csv")

#Crear grafico de barras
sns.lineplot(x="fecha", y="pedos", data=df)

#Crear un punto del pedo mayor
plt.plot("01-09",17,"o")

#Mostrar grafico
plt.show()