import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leer csd de pedos
df=pd.read_csv("ejercicios_3\\ingresos.csv")

#Crear grafico de barras
sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos=df["ingresos"].sum()
print(f"El total de ingresos es de: ${total_ingresos} USD")

#Mostrar grafico
plt.show()