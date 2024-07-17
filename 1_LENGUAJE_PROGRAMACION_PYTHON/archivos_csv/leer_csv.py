#Profesionalmente se usa pandas
#Pandas hace los mismo pero mejor que la libreia csv

import csv

with open("archivos_csv\\datos.csv") as archivo:
    reader=csv.reader(archivo)
    for row in reader:
        print(row)