# While con Switch Anidado para Máquina Virtual?
# Pilas de operadores, saltos, operandos y tipos
from Lexer import *
from Parser import *

from functions import importData, print_tuple
from VirtualMachine import virtual_machine

try:
  # Import the Data from the File
  data = importData("Example3")

  # Build the lexer and parser
  lexer = lex.lex()
  parser = yacc.yacc()

  result = parser.parse(data, lexer=lexer)
  virtual_machine()

except Exception as e:
  print(e)

try:
  # Print Synthactic Tree
  print("\n******** Synthactic Tree ********")
  print_tuple(result)
except Exception as e:
  print(e)

try:
  # Print the Quadruples
  print("\n******** Quadruples ********")
  quadruple.print()
except Exception as e:
  print(e)

try:
  # Print the Variables and it's values
  print("\n******** Variables ********")
  symbols_copy.print()
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
