import re

# regex = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
regex = r'\'.\''

# Ejemplo de uso
numero = "'0'"
es = re.match(regex, numero)
if es:
  print("Válido.")
else:
  print("No válido.")
# def es_entero(cadena):
#     return cadena.isdigit()

# # Ejemplo de uso
# cadena1 = "1234.0"
# cadena2 = "3.14"
# cadena3 = "abcd"

# print(es_entero(cadena1))  # True
# print(es_entero(cadena2))  # False
# print(es_entero(cadena3))  # False
