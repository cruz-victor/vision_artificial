import re

texto="Hola Victor eres un crack"

resultado=re.findall("\w", texto)
print(resultado)