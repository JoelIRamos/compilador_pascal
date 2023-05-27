# Imprimir Lista de Cuadruplos
# While con Switch Anidado para Máquina Virtual?
# Tabla se símbolos, id, valor actual, tipo de dato, posici´øn
# Pilas de operadores, saltos, operandos y tipos
# Pilas () -> Cuadruplos -> Correr Código (con muucha lógica)
from Lexer import *
from Parser import *

from functions import importData

try:
  # Build the lexer and parser
  data = importData("Example1")

  lexer = lex.lex()
  lexer.input(data)

  parser = yacc.yacc()
  result = parser.parse(data)

  # print(result)
  lexer.input(data)

except Exception as e:
  print(e)

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok)
