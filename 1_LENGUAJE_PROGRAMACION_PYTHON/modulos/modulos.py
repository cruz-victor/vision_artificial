# import modulo_saludar as m_saludar
from modulo_saludar import greetings as saludar_spanish, greatings_in_english as saludar_english
import modulo_saludar as modulo

# saludo=m_saludar.greetings("Elon Victor")
# saludo=greetings("Elon Victor")
# print(saludo)

# saludo_english=greatings_in_english("Juan Quintanilla")
# print(saludo_english)

saludo= saludar_spanish("Victor")
print(saludo)
saludo_dos=saludar_english("Juan")
print(saludo_dos)

print(dir(modulo))
print(modulo.hi_programmer)

