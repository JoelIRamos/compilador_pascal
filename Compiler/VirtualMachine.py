# from Quadruples import Quadruples
# from Symbols import Symbols

# def virtual_machine(quads):
#   end = False
#   line = 0
#   print(' | lin | Opr | Arg1 | Arg2 | Res | ')
#   while (not end):
#     operator, argument1, argumen2, result = quads[line]
#     print(" | ", line, " | ", operator, " | ", argument1, " | ", argumen2,
#           " | ", result, " | ")
#     if (operator == None):
#       end = True
#     line += 1

# If the arguent is an string, it could be either a string value or a variable
# if (isinstance(argument1, str)):
#   # If it doesn't begin with " it's a variable
#   if (argument1[0] != '"'):
#     print(variables[argument1])
#   else:
#     # Print string value without ""
#     print(argument1[1:-1])
# else:

from Parser import symbols_copy as variables
from Parser import quadruple as quadruples


def virtual_machine():
  end = False
  line = 0
  print('Starting to Run...')
  while (not end):
    # Obtain each value in a quadruple
    operator, argument1, argument2, result = quadruples.quadruples[line]
    # print(quadruples.quadruples[line])
    # Get the real values of the arguments
    argument1, argument2 = variables.getRealValues(argument1, argument2)
    # print(argument1, " ", argument2)
    argument1_type, argument2_type, result_type = variables.getDataTypes(
      argument1, argument2, result)
    # print(argument1_type, " ", argument2_type, " ", result_type)

    # For each case of quadruples
    if (operator == 'goToF'):
      if (not argument1):
        line = result
        continue
    elif (operator == 'goTo'):
      line = result
      continue
    elif (operator == ':='):
      res = argument1
    elif (operator == '>'):
      res = argument1 > argument2
    elif (operator == '<'):
      res = argument1 < argument2
    elif (operator == '>='):
      res = argument1 >= argument2
    elif (operator == '<='):
      res = argument1 <= argument2
    elif (operator == '='):
      res = argument1 == argument2
    elif (operator == '+'):
      res = argument1 + argument2
    elif (operator == '-'):
      res = argument1 - argument2
    elif (operator == '*'):
      res = argument1 * argument2
    elif (operator == '/'):
      if argument2 == 0:
        raise Exception("Running Error: can't be divided by zero")
      res = argument1 / argument2
      pass
    elif (operator == 'and'):
      res = argument1 and argument2
    elif (operator == 'or'):
      res = argument1 or argument2
    elif (operator == 'write'):
      print(argument1)
      line += 1
      continue
    elif (operator == None):
      end = True
    else:
      raise Exception("CE: Case not contemplated")

    variables.symbols[result] = [res, result_type, None]
    line += 1
