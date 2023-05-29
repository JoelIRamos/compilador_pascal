# Imprimir Lista de Cuadruplos
# While con Switch Anidado para Máquina Virtual?
# Tabla se símbolos, id, valor actual, tipo de dato, posici´øn
# Pilas de operadores, saltos, operandos y tipos
# Pilas () -> Cuadruplos -> Correr Código (con muucha lógica)
from Lexer import *
from Parser import *

from functions import importData

try:
  # Import the Data from the File
  data = importData("Example")

  # Build the lexer and parser
  lexer = lex.lex()
  parser = yacc.yacc()

  # lexer.input(data)
  result = parser.parse(data, lexer=lexer)

  # print(quad)
  print(result)

except Exception as e:
  print(e)

# newlexer = lex.lex()
# newlexer.input(data)
# # Tokenize
# while True:
#   tok = newlexer.token()
#   if not tok:
#     break  # No more input
#   print(tok)

# from symbols import Symbols
# from quadruples import Quadruples

# quad = Quadruples()
# symb = Symbols()
# temporal = symb.generateTemporal()
# quad.addQuadruples('+', 'b', 'c', temporal)
# quad.addQuadruples(':=', temporal, None, 'a')

# print("Quadruples: ", quad)
# print("Symbols: ", symb)
