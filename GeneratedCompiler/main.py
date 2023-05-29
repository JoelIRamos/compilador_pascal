from lexer import *
from parser import *

from functions import importData

# ----------------- Lexer and Parser Initialization -----------------

# Build the lexer
lexer = lex.lex()
# newlexer = lexer.clone()

# Build the parser
parser = yacc.yacc()

# ----------------- Testing -----------------

code = importData("Example4")

# Parse the code
parser.parse(code, lexer=lexer)

# newlexer.input(code)

# # Tokenize
# while True:
#   tok = newlexer.token()
#   if not tok:
#     break  # No more input
#   print(tok)
# symbol_table = {}

print(quadruples)

for quad in quadruples:
  print(quad)