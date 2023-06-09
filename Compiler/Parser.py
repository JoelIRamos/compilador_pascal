import ply.yacc as yacc
from Lexer import tokens
from Quadruples import Quadruples
from Symbols import Symbols
from functions import debug_print, simplifyTuple, separateVariables, checkDataType

# Precedence of each operators (tokens)
precendence = (
  ('right', 'ASSIGN'),
  ('left', 'AND', 'OR'),
  ('left', 'EQUAL'),
  ('left', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  ('left', 'PLUSPLUS', 'MINUSMINUS'),
  ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)

# ----------------- Semantic Structure Helpers -----------------

quadruple = Quadruples()
# quadruple.addQuadruples(operator, left, right, result)
stack = []
jumps = []
symbols = Symbols()
symbols_copy = Symbols()
for_id = ''

# ----------------- Grammar Rules -----------------


# ++++++++ Program +++++++++++
def p_program(p):
  '''
  Program : PROGRAM ID LEFTBRACKET variable block RIGHTBRACKET
  '''
  debug_print("program")
  p[4] = tuple(separateVariables(p[4]))
  p[0] = (p[1], p[2], p[4], p[5])
  quadruple.addQuadruples(None, None, None, None)


def p_program_without_vars(p):
  '''
  Program : PROGRAM ID LEFTBRACKET block RIGHTBRACKET
  '''
  debug_print("program")
  p[0] = (p[1], p[2], p[4])


# ++++++++ VARIABLE +++++++++++
def p_variable(p):
  '''
  variable : VAR variables COLON datatype SEMICOLON
  '''
  debug_print("variable")
  # Format the tuple in a better way for the diferent variables
  p[2] = simplifyTuple(p[2])
  p[0] = (p[1], p[2], p[4])
  # For each Variable, add it to the symbols
  for variable in p[2]:
    symbols.writeSymbol(str(variable), None, p[4], None)
    symbols_copy.writeSymbol(str(variable), None, p[4], None)


def p_variable_repetition(p):
  '''
  variable : variable variable
  '''
  debug_print("variable")
  # Combining tuplets, so they end up as a big plain tuple
  if (isinstance(p[1][0], tuple) and isinstance(p[2][0], tuple)):
    result = p[1] + p[2]
  elif isinstance(p[1][0], tuple):
    result = p[1] + (p[2])
  elif isinstance(p[2][0], tuple):
    result = (p[1]) + (p[2])
  else:
    result = (p[1]) + (p[2])
  p[0] = result


def p_variables(p):
  '''
  variables : ID
  '''
  debug_print("variables")
  p[0] = p[1]


def p_variables_repetition(p):
  '''
  variables : variables COMMA variables
  '''
  debug_print("variables")
  p[0] = (p[1], p[3])


# Here is defined the diferent datatypes that the variables can be
def p_datatype(p):
  '''
  datatype : INT
           | REAL
           | BOOL
           | STR
  '''
  debug_print("datatype")
  p[0] = p[1]


# ++++++++ BLOCK +++++++++++
def p_block(p):
  '''
  block : BEGIN SEMICOLON statement END SEMICOLON
  '''
  debug_print("block")
  p[0] = (p[1], p[3], p[4])


# ++++++++ STATEMENT +++++++++++
def p_statement(p):
  '''
  statement : writestatement
            | assignstatement
            | ifstatement
            | whileloop
            | forloop
  '''
  debug_print("statement")
  p[0] = p[1]


def p_statements(p):
  '''
  statement : statement statement
  '''
  debug_print("statements")
  # Combine tuples in a way that each statements end up in tuple in the block tuple or the statements for other statements structures
  if (isinstance(p[1][0], tuple) and isinstance(p[2][0], tuple)):
    result = p[1] + p[2]
  elif isinstance(p[1][0], tuple):
    result = p[1] + tuple([p[2]])
  elif isinstance(p[2][0], tuple):
    result = tuple([p[1]]) + (p[2])
  else:
    result = tuple([p[1], p[2]])
  p[0] = result


# ++++++++ WRITE +++++++++++
def p_writestatement(p):
  '''
  writestatement : WRITE LEFTPARENTHESIS expression point_ae RIGHTPARENTHESIS SEMICOLON
  '''
  debug_print("writestatement")
  p[0] = (p[1], p[3])
  quadruple.addQuadruples(p[1], p[4], None, None)


# ++++++++ ASSIGMENT +++++++++++
def p_assignstatement_classic(p):
  '''
  assignstatement : ID ASSIGN expression point_ae SEMICOLON
  '''
  debug_print("assignstatement_classic")
  p[0] = (p[2], p[1], p[3])
  # Check that the value is the same datatype as of the variable
  datatypes = checkDataType(symbols.getSymbol(p[1]), symbols.getSymbol(p[4]))
  if (datatypes):
    quadruple.addQuadruples(p[2], p[4], None, p[1])
  else:
    raise Exception(p[1], " datatype mismatch the expresion datatype")


def p_assignstatement_increment_decrement(p):
  '''
  assignstatement : ID PLUSPLUS SEMICOLON
                  | ID MINUSMINUS SEMICOLON
  '''
  debug_print("assignstatement_increment_decrement")

  # In case ++ -> id = id + 1. In case -- -> id = id - 1.
  if (p[2] == '++'):
    p[0] = (':=', p[1], ('+', p[1], 1))
    quadruple.addQuadruples('+', p[1], 1, p[1])
  else:
    p[0] = (':=', p[1], ('-', p[1], 1))
    quadruple.addQuadruples('-', p[1], 1, p[1])


# ++++++++ IF +++++++++++
def p_ifstatement(p):
  '''
  ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS point_if_then_ini THEN LEFTBRACKET statement RIGHTBRACKET elsestatement
  '''
  debug_print("ifstatement")
  p[0] = (p[1], p[3], p[6], p[7], p[8], p[9])
  if p[10] == None:
    quadruple.fillQuadruples(jumps.pop(), quadruple.counter)


def p_if_else_statement(p):
  '''
  elsestatement : ELSE point_else_ini LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("if_else_statement")
  p[0] = (p[1], p[2], p[4], p[5])
  quadruple.fillQuadruples(jumps.pop(), quadruple.counter)


def p_if_else_statement_none(p):
  '''
  elsestatement : 
  '''
  debug_print("p_if_else_statement_none")
  p[0] = None


def p_point_if_then_ini(p):
  '''
  point_if_then_ini : 
  '''
  var = stack.pop()
  symbol = symbols.getSymbol(var)
  if symbol[1] == 'bool':
    if symbol[0] != None:
      var = symbol[0]

    quadruple.counter
    jumps.append(quadruple.counter)
    quadruple.addQuadruples('goToF', var, None, None)
  else:
    raise Exception(
      "The expression for the IF Statement must resolve in a boolean value")
  return


def p_point_else_ini(p):
  '''
  point_else_ini : 
  '''
  p[0] = None
  jump = jumps.pop()
  jumps.append(quadruple.counter)
  quadruple.addQuadruples('goTo', None, None, None)
  quadruple.fillQuadruples(jump, quadruple.counter)
  return


# ++++++++ WHILE +++++++++++
def p_whileloop(p):
  '''
  whileloop : WHILE LEFTPARENTHESIS point_first_exp expression RIGHTPARENTHESIS DO point_while LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("whileloop")
  p[0] = (p[1], p[4], p[6], p[8], p[9], p[10])
  quadruple.addQuadruples('goTo', None, None, jumps.pop())
  quadruple.fillQuadruples(jumps.pop(), quadruple.counter)


def p_point_while(p):
  '''
  point_while : 
  '''
  p[0] = None
  var = stack.pop()
  symbol = symbols.getSymbol(var)
  if symbol[1] == 'bool':
    if symbol[0] != None:
      var = symbol[0]

    # Line of the first expresion
    start = jumps.pop()
    # Must be appended first because gotoF is the last jump
    jumps.append(quadruple.counter)
    jumps.append(start)
    quadruple.addQuadruples('goToF', var, None, None)

  else:
    raise Exception(
      "The expression for the While Statement must resolve in a boolean value")
  return


def p_point_first_exp(p):
  '''
  point_first_exp :
  '''
  p[0] = None
  # Line of the first expresion
  jumps.append(quadruple.counter)


# ++++++++ FOR +++++++++++
def p_forloop(p):
  '''
  forloop : FOR LEFTPARENTHESIS assignstatement_for SEMICOLON point_for_pre_exp expression point_for_end_exp SEMICOLON increment_decrement RIGHTPARENTHESIS LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("forloop")
  # Add the increment or decrement quadruple
  if p[9][1] == '++':
    quadruple.addQuadruples('+', p[9][0], 1, p[9][0])
  elif p[9][1] == '--':
    quadruple.addQuadruples('-', p[9][0], 1, p[9][0])
  else:
    raise Exception("CE:", p[9][1], 'must be either ++ or --')

  # Add the got to comparison
  quadruple.addQuadruples('goTo', None, None, p[5])
  quadruple.fillQuadruples(jumps.pop(), quadruple.counter)
  p[0] = (p[1], p[3], p[4], p[6], p[8], p[9], p[11], p[12], p[13])


def p_assignstatement_for(p):
  '''
  assignstatement_for : ID ASSIGN expression point_ae
  '''
  debug_print("assignstatement_for")
  p[0] = (p[2], p[1], p[3])

  # Check that the value is the same datatype as of the variable
  datatypes = checkDataType(symbols.getSymbol(p[1]), symbols.getSymbol(p[4]))
  if (datatypes):
    if datatypes[0] == 'int':
      quadruple.addQuadruples(p[2], p[4], None, p[1])
    else:
      raise Exception(
        "Error with", p[1],
        ". In For Loop, the variable datatype must be an integer")
  else:
    raise Exception("For Loop Error: ", p[1],
                    " datatype mismatch the first expresion datatype")


# Return the index where the comparison begin
def p_point_for_pre_exp(p):
  '''
  point_for_pre_exp :
  '''
  p[0] = quadruple.counter


def p_point_for_end_exp(p):
  '''
  point_for_end_exp : point_ae
  '''
  symbol = symbols.getSymbol(p[1])
  # print("Symbol:", symbol, "var: ", p[1])
  if symbol[1] == 'bool':
    jumps.append(quadruple.counter)
    quadruple.addQuadruples('goToF', p[1], None, None)
  else:
    raise Exception(
      "For Error: second expression must resolve to a boolean value")
  p[0] = None


def p_increment_decrement(p):
  '''
  increment_decrement : ID PLUSPLUS
                      | ID MINUSMINUS
  '''
  debug_print("increment_decrement")
  symbol = symbols.getSymbol(p[1])
  if symbol:
    if symbol[1] == 'int':
      p[0] = (p[1], p[2])
    else:
      raise Exception(p[1], "must be an integer for the For Loop")
  else:
    raise Exception(p[1], "wasn't defined in the scope")


# ++++++++ EXPRESSIONS +++++++++++
# The output of an expresion is either a variable of the program, a temporal variable or a value of the datatypes
def p_expression(p):
  '''
  expression : logical_expression 
             | relational_expression 
             | arithmetic_expression 
             | expression_id
  '''
  debug_print("expression")
  p[0] = p[1]


# ======== STRING ========
def p_expression_string(p):
  '''
  expression : STRING
  '''
  debug_print("expression_string")
  p[0] = p[1]
  temporal = symbols.generateTemporal()
  symbols.writeSymbol(temporal, p[1], 'str', None)
  stack.append(temporal)


# ======== LOGICAL ========
def p_logical_expression_log2rel(p):
  '''
  logical_expression : relational_expression 
  '''
  p[0] = p[1]


def p_logical_expression(p):
  '''
  logical_expression : relational_expression point_ae AND relational_expression point_ae
                     | relational_expression point_ae OR relational_expression point_ae
                     | logical_expression point_ae AND logical_expression point_ae
                     | logical_expression point_ae OR logical_expression point_ae
  '''
  debug_print("logical_expression")
  p[0] = (p[3], p[1], p[4])

  # Create the temporal variable for the result of the operation
  temporal = symbols.generateTemporal()

  # Add it to the Stack
  stack.append(temporal)

  # Crearte the quadruple
  quadruple.addQuadruples(p[3], p[2], p[5], temporal)

  # Obtain the symbols of each "arith_expression"
  datatypes = checkDataType(symbols.getSymbol(p[2]), symbols.getSymbol(p[5]))
  # Validate the datatypes of the operation match
  if (datatypes):
    # Validate the datatypes are boolean (True/False)
    if (datatypes[0] == 'bool' and datatypes[1] == 'bool'):
      symbols.writeSymbol(temporal, None, 'bool', None)
    else:
      raise Exception(
        "DataType mismatch, logical operators can only compare logical values (True/False)."
      )
  else:
    raise Exception("DataType mismatch with ", p[1], " and ", p[4],
                    ". They are incompatible.")


def p_logical_expression_parenthesis(p):
  '''
  logical_expression : LEFTPARENTHESIS logical_expression RIGHTPARENTHESIS
  '''
  debug_print("logical_expression_parenthesis")
  p[0] = p[2]


# ======== RELATIONAL ========
def p_relational_expression(p):
  '''
  relational_expression : arithmetic_expression point_ae GREATER arithmetic_expression point_ae
                        | arithmetic_expression point_ae LESSER arithmetic_expression point_ae
                        | arithmetic_expression point_ae GREATEREQUAL arithmetic_expression point_ae
                        | arithmetic_expression point_ae LESSEREQUAL arithmetic_expression point_ae
                        | arithmetic_expression point_ae EQUAL arithmetic_expression point_ae
  '''
  debug_print("relational_expression")
  p[0] = (p[3], p[1], p[4])
  # Create the temporal variable for the result of the operation
  temporal = symbols.generateTemporal()

  # Add it to the Stack
  stack.append(temporal)

  # Crearte the quadruple
  quadruple.addQuadruples(p[3], p[2], p[5], temporal)

  # Obtain the symbols of each "arith_expression"
  datatypes = checkDataType(symbols.getSymbol(p[2]), symbols.getSymbol(p[5]))

  # Validate the datatypes of the operation match
  if (datatypes):
    # Validate the datatypes are arithmetic (numbers)
    if ((datatypes[0] == 'int' or datatypes[0] == 'real')
        and (datatypes[1] == 'int' or datatypes[1] == 'real')):
      symbols.writeSymbol(temporal, None, 'bool', None)
    else:
      # Case for when a variable is a string
      if (p[3] == '=' and datatypes == ['str', 'str']):
        symbols.writeSymbol(temporal, None, 'bool', None)
      else:
        raise Exception(
          "DataType mismatch, relational operators can only compare arithmetic values."
        )
  else:
    raise Exception("DataType mismatch with ", p[1], " and ", p[4],
                    ". They are incompatible.")


# Strings can only be compared with the equal relational operator
def p_relational_expression_string(p):
  '''
  relational_expression : STRING EQUAL STRING
  '''
  debug_print("relational_expression_string")
  p[0] = (p[2], p[1], p[3])

  # Create the temporal variable for the result of the operation
  temporal = symbols.generateTemporal()

  quadruple.addQuadruples(p[2], p[1], p[3], temporal)

  # Add it to the Stack
  stack.append(temporal)

  # Add it to the symbol table
  symbols.writeSymbol(temporal, None, 'bool', None)


def p_relational_expression_parenthesis(p):
  '''
  relational_expression : LEFTPARENTHESIS relational_expression RIGHTPARENTHESIS
  '''
  debug_print("relational_expression_parenthesis")
  p[0] = p[2]


def p_relational_expression_unit(p):
  '''
  relational_expression : BOOLEAN
  '''
  debug_print("relational_expression_unit")
  p[0] = p[1]
  temporal = symbols.generateTemporal()
  symbols.writeSymbol(temporal, p[1], 'bool', None)
  stack.append(temporal)


# ======== ARITHMETIC ========
def p_arithmetic_expression(p):
  '''
  arithmetic_expression : arithmetic_expression point_ae PLUS arithmetic_expression point_ae
                        | arithmetic_expression point_ae MINUS arithmetic_expression point_ae
                        | arithmetic_expression point_ae TIMES arithmetic_expression point_ae
                        | arithmetic_expression point_ae DIVIDE arithmetic_expression point_ae
  '''
  debug_print("arithmetic_expression")
  p[0] = (p[3], p[1], p[4])

  # Create the temporal variable for the result of the operation
  temporal = symbols.generateTemporal()

  # Add it to the Stack
  stack.append(temporal)

  # Crearte the quadruple
  quadruple.addQuadruples(p[3], p[2], p[5], temporal)

  # Obtain the symbols of each "arith_expression"
  datatypes = checkDataType(symbols.getSymbol(p[2]), symbols.getSymbol(p[5]))

  # Validate the datatypes of the operation match
  if (datatypes):
    # Verify the datatype is of a number
    if ((datatypes[0] == 'int' or datatypes[0] == 'real')
        and (datatypes[1] == 'int' or datatypes[1] == 'real')):
      # If one of the datatypes is a Real Number, then the expression is Real also
      if datatypes[0] == 'int' and datatypes[1] == 'int':
        symbols.writeSymbol(temporal, None, 'int', None)
      else:
        symbols.writeSymbol(temporal, None, 'real', None)
    else:
      raise Exception(
        "DataType mismatch, arithmetic operators can only operate on arithmetic values."
      )
  else:
    raise Exception("DataType mismatch with ", p[1], " and ", p[4])


def p_arithmetic_expression_parenthesis(p):
  '''
  arithmetic_expression : LEFTPARENTHESIS arithmetic_expression RIGHTPARENTHESIS
  '''
  debug_print("arithmetic_expression_parenthesis")
  p[0] = p[2]


def p_arithmetic_expression_id(p):
  '''
  arithmetic_expression : expression_id
  '''
  p[0] = p[1]


def p_arithmetic_expression_integer(p):
  '''
  arithmetic_expression : INTEGER
  '''
  p[0] = p[1]
  temporal = symbols.generateTemporal()
  symbols.writeSymbol(temporal, p[1], 'int', None)
  stack.append(temporal)


def p_arithmetic_expression_number(p):
  '''
  arithmetic_expression : NUMBER
  '''
  p[0] = p[1]
  temporal = symbols.generateTemporal()
  symbols.writeSymbol(temporal, p[1], 'real', None)
  stack.append(temporal)


def p_expression_id(p):
  '''
  expression_id : ID
  '''
  p[0] = p[1]
  var = symbols.getSymbol(p[1])

  # Si la var fue encontrada
  if var:
    # Add it to the stack
    stack.append(p[1])
  else:
    raise Exception(str(p[1]) + " was not defined")
  # ToDo: CHECK ALL THE DATATYPES


# ++++++++ EMPTY +++++++++++
def p_empty(p):
  '''
  empty :
  '''
  p[0] = None
  debug_print("empty")
  pass


# ++++++++ ERROR +++++++++++
def p_error(p):
  if p is not None:
    raise Exception("Sintaxis Error: Line ", p.lineno, " illegal token ",
                    p.value)
    # "Sintaxis Error with", p.value)
  else:
    raise Exception('Unexpected end of input')


# Hacer pop al último valor y guardarlo en p[0]
# También revisa que el valor exista en la tabla de simbolos
# Y si el valor era contante en temporal, regresa la constante
def p_point_ae(p):
  '''
  point_ae : 
  '''
  var = stack.pop()
  symbol = symbols.getSymbol(var)
  if symbol:
    if symbol[0] == None:
      p[0] = var
    else:
      p[0] = symbol[0]
  else:
    raise Exception("CE: ", var, "was not defined")
  return
