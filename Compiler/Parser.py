import ply.yacc as yacc
from Lexer import tokens
# from quadruples import Quadruples
from functions import debugPrint as debug_print
from functions import simplifyTuple
from functions import separateVariables
        
# Precedencia de cada token, var, program, id, etc.
precendence = (
  ('right', 'ASSIGN'),
  ('left', 'AND', 'OR'),
  ('left', 'DISTINCT', 'EQUAL'),
  ('left', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  ('left', 'PLUSPLUS', 'MINUSMINUS'),
  ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)

# ----------------- Grammar Rules -----------------


def p_program(p):
  '''
  Program : PROGRAM ID LEFTBRACKET variable block RIGHTBRACKET
  '''
  debug_print("program")
  p[4] = tuple(separateVariables(p[4]))
  p[0] = (p[1], p[2], p[4], p[5])

def p_program_without_vars(p):
  '''
  Program : PROGRAM ID LEFTBRACKET block RIGHTBRACKET
  '''
  debug_print("program")
  p[0] = (p[1], p[2], p[4])


def p_variable(p):
  '''
  variable : VAR variables COLON datatype SEMICOLON
  '''
  debug_print("variable")
  p[2] = simplifyTuple(p[2])
  p[0] = (p[1], p[2], p[4])


def p_variable_repetition(p):
  '''
  variable : variable variable
  '''
  debug_print("variable")
  # p[0] = (p[1], p[2])
  if (isinstance(p[1][0], tuple) and isinstance(p[2][0], tuple)):
    result = p[1] + p[2]
  elif isinstance(p[1][0], tuple):
    result = p[1] + (p[2])
    print(result)
  elif isinstance(p[2][0], tuple):
    result = (p[1]) + (p[2])
    print(result)
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


def p_datatype(p):
  '''
  datatype : INT
           | REAL
           | BOOL
           | STR
  '''
  debug_print("datatype")
  p[0] = p[1]


def p_block(p):
  '''
  block : BEGIN SEMICOLON statement END SEMICOLON
  '''
  debug_print("block") 
  p[0] = (p[1], p[3], p[4])


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


# ToDo como hago esto? ()(()()) -> ()()() y (()())() -> ()()()
def p_statements(p):
  '''
  statement : statement statement
  '''
  debug_print("statements")
  # p[0] = (p[1], p[2])
  if (isinstance(p[1][0], tuple) and isinstance(p[2][0], tuple)):
    result = p[1] + p[2]
    print(result)
  elif isinstance(p[1][0], tuple):
    result = p[1] + tuple([p[2]])
    # print(result)
  elif isinstance(p[2][0], tuple):
    result = tuple([p[1]]) + (p[2])
    print(p[1])
    print(p[2])
    print(result)
  else:
    result = tuple([p[1],p[2]])
    print(result)
  p[0] = result


def p_writestatement(p):
  '''
  writestatement : WRITE LEFTPARENTHESIS expression RIGHTPARENTHESIS SEMICOLON
  '''
  debug_print("writestatement")
  p[0] = (p[1], p[3])


def p_assignstatement_classic(p):
  '''
  assignstatement : ID ASSIGN expression SEMICOLON
  '''
  debug_print("assignstatement_classic")
  p[0] = (p[2], p[1], p[3])


def p_assignstatement_increment_decrement(p):
  '''
  assignstatement : ID PLUSPLUS SEMICOLON
                  | ID MINUSMINUS SEMICOLON
  '''
  debug_print("assignstatement_increment_decrement")
  p[0] = (p[2], p[1])


def p_ifstatement(p):
  '''
  ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS THEN LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("ifstatement")
  p[0] = (p[1], p[3], p[5], p[6], p[7], p[8])


def p_if_else_statement(p):
  '''
  ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS THEN LEFTBRACKET statement RIGHTBRACKET ELSE LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("if_else_statement")
  p[0] = (p[1], p[3], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])


def p_whileloop(p):
  '''
  whileloop : WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS DO LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("whileloop")
  p[0] = (p[1], p[3], p[5], p[6], p[7], p[8])


def p_forloop(p):
  '''
  forloop : FOR LEFTPARENTHESIS ID ASSIGN expression SEMICOLON expression SEMICOLON ID increment_decrement RIGHTPARENTHESIS LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("forloop")
  p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11],
          p[12], p[13], p[14])


# **************************************************
def p_increment_decrement(p):
  '''
  increment_decrement : PLUSPLUS
                      | MINUSMINUS
  '''
  debug_print("formodifier")
  p[0] = p[1]


def p_expression(p):
  '''
  expression : logical_expression 
             | relational_expression 
             | arithmetic_expression 
             | ID
             | STRING
  '''
  debug_print("expression")
  p[0] = p[1]


def p_logical_expression(p):
  '''
  logical_expression : relational_expression AND relational_expression
                     | relational_expression OR relational_expression
  '''
  debug_print("logical_expression")
  p[0] = (p[2], p[1], p[3])


def p_logical_expression_parenthesis(p):
  '''
  logical_expression : LEFTPARENTHESIS logical_expression RIGHTPARENTHESIS
  '''
  debug_print("logical_expression_parenthesis")
  p[0] = p[2]


def p_relational_expression(p):
  '''
  relational_expression : arithmetic_expression GREATER arithmetic_expression
                        | arithmetic_expression LESSER arithmetic_expression
                        | arithmetic_expression GREATEREQUAL arithmetic_expression
                        | arithmetic_expression LESSEREQUAL arithmetic_expression
                        | arithmetic_expression EQUAL arithmetic_expression
                        | STRING EQUAL STRING
  '''
  debug_print("relational_expression")
  p[0] = (p[2], p[1], p[3])


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


def p_arithmetic_expression(p):
  '''
  arithmetic_expression : arithmetic_expression PLUS arithmetic_expression
                        | arithmetic_expression MINUS arithmetic_expression
                        | arithmetic_expression TIMES arithmetic_expression
                        | arithmetic_expression DIVIDE arithmetic_expression
  '''
  debug_print("arithmetic_expression")
  p[0] = (p[2], p[1], p[3])


def p_arithmetic_expression_parenthesis(p):
  '''
  arithmetic_expression : LEFTPARENTHESIS arithmetic_expression RIGHTPARENTHESIS
  '''
  debug_print("arithmetic_expression_parenthesis")
  p[0] = p[2]


def p_arithmetic_expression_modifier(p):
  '''
  arithmetic_expression : ID
                        | INTEGER
                        | NUMBER
  '''
  p[0] = p[1]


def p_empty(p):
  '''
  empty :
  '''
  p[0] = None
  debug_print("empty")
  pass


def p_error(p):
  if p is not None:
    print("Line ", p.lineno, " illegal token ", p.value)
    print("Sintaxis Error with", p)
  else:
    print('Unexpected end of input')
