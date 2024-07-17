# import modulo_saludar as m_saludar
from  funciones_buenas.modulo_saludar import greetings as saludar_spanish, greatings_in_english as saludar_english
import funciones_buenas.modulo_saludar as modulo
import sys

# saludo=m_saludar.greetings("Elon Victor")
# saludo=greetings("Elon Victor")
# print(saludo)

# saludo_english=greatings_in_english("Juan Quintanilla")
# print(saludo_english)

saludo= saludar_spanish("Victor")
print(saludo)
saludo_dos=saludar_english("Juan")
print(saludo_dos)

# print(dir(modulo))
# print(modulo.hi_programmer)
#Despues de agrear la ruta externa se puede usar la funcion del modulo
sys.path.append("c:\\x_vision_artificial\\1_LENGUAJE_PROGRAMACION_PYTHON\\otros_modulos")
print(sys.builtin_module_names)
print(sys.path)

# import otros_modulos.modulo_saludar_2
# print(modulo_saludar_2.greetings)
