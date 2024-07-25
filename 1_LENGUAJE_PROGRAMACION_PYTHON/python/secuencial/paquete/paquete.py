#Un paquete es una carpeta con varios modulos
#Un paquete tiene que tener el archivo __init__.py
#Un subpaquete tiene que tener el __init__.py

import paquete.saludar_spanish
import paquete.saludar_english

# print(type(paquete))
print(paquete.saludar_spanish.saludar("Vic"))
print(paquete.saludar_english.greetings("Elon"))

# print(paquete.__path__)