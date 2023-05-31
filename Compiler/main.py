# While con Switch Anidado para Máquina Virtual?
# Pilas de operadores, saltos, operandos y tipos
from Lexer import *
from Parser import *

from functions import importData
from functions import print_tuple

try:
  # Import the Data from the File
  data = importData("Example2")

  # Build the lexer and parser
  lexer = lex.lex()
  parser = yacc.yacc()

  # lexer.input(data)
  result = parser.parse(data, lexer=lexer)

  # print(quad)
  # print(result)
  print_tuple(result)


  

except Exception as e:
  print(e)
# print("-----")
# print(symbols)
# quadruple.print()

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
