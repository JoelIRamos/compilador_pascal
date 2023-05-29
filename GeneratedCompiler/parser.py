import ply.yacc as yacc
from semantic import *
from quadruples import Quadruples

from functions import debugPrint as debug_print

# ----------------- Parser -----------------

# Precedence of each token
precedence = (
  ('right', 'ASSIGN'),
  ('left', 'AND', 'OR'),
  ('left', 'EQUAL'),
  ('left', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  ('left', 'PLUSPLUS', 'MINUSMINUS'),
  ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)

quad = Quadruples()

# ----------------- Grammar Rules -----------------


def p_program(p):
  '''
    Program : PROGRAM ID LEFTBRACKET variable block RIGHTBRACKET
  '''
  debug_print("program")


def p_variable(p):
  '''
    variable : VAR ID variables COLON datatype SEMICOLON variable
             | empty
    '''
  debug_print("variable")


def p_variables(p):
  '''
    variables : COMMA ID variables
              | empty
    '''
  debug_print("variables")


def p_datatype(p):
  '''
    datatype : INT
             | REAL
             | BOOL
             | STR
    '''
  debug_print("datatype")


def p_block(p):
  '''
    block : BEGIN SEMICOLON statement END SEMICOLON
    '''
  debug_print("block")


def p_statement(p):
  '''
    statement : writestatement statement
              | assignstatement statement
              | ifstatement statement
              | whileloop statement
              | forloop statement
              | empty
    '''
  debug_print("statement")


def p_writestatement(p):
  '''
    writestatement : WRITE LEFTPARENTHESIS expression RIGHTPARENTHESIS SEMICOLON
    '''
  debug_print("writestatement")


def p_assignstatement(p):
  '''
    assignstatement : ID ASSIGN expression SEMICOLON
    '''
  debug_print("assignstatement")
  # gen_quad(p[2], p[3], None, p[1])


def p_ifstatement(p):
  '''
    ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS THEN LEFTBRACKET statement RIGHTBRACKET elsestatement
    '''
  debug_print("ifstatement")
  # if p[3]:
  #   quad_index = gen_quad_jump('if', p[3], None, None)
  #   backpatch(quad_index, len(quadruples))
  #   p[7]
  # else:
  #   quad_index = gen_quad_placeholder('if', p[3], None)
  #   p[7]
  #   jump_index = gen_quad_jump('goto', None, None, None)
  #   backpatch(quad_index, len(quadruples))
  #   backpatch(jump_index, len(quadruples))


def p_elsestatement(p):
  '''
    elsestatement : ELSE LEFTBRACKET statement RIGHTBRACKET
                  | empty
    '''
  debug_print("elsestatement")
  # if p[1] is not None:
  #   p[3]


def p_whileloop(p):
  '''
    whileloop : WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS DO LEFTBRACKET statement RIGHTBRACKET
    '''
  debug_print("whileloop")
  # quad_index = len(quadruples)
  # if p[3]:
  #   quad_index = gen_quad_jump('while', p[3], None, None)
  #   backpatch(quad_index, len(quadruples))
  #   p[7]
  #   gen_quad_jump('goto', None, None, quad_index)


def p_forloop(p):
  '''
    forloop : FOR LEFTPARENTHESIS ID ASSIGN expression SEMICOLON expression SEMICOLON formodifier RIGHTPARENTHESIS LEFTBRACKET statement RIGHTBRACKET
    '''
  debug_print("forloop")
  for_init = p[4]
  for_expr = p[6]
  for_mod = p[9]
  for_statement = p[12]

  if for_init:
    gen_quad('=', for_init, None, p[3])

  quad_index = len(quadruples)
  if for_expr:
    quad_index = gen_quad_jump('for', for_expr, None, None)
    backpatch(quad_index, len(quadruples))
    for_statement
    if for_mod:
      gen_quad(for_mod, p[3], 1, p[3])
    gen_quad_jump('goto', None, None, quad_index)


def p_formodifier(p):
  '''
    formodifier : ID PLUSPLUS
                | ID MINUSMINUS
    '''
  debug_print("formodifier")
  p[0] = '+' if p[2] == '++' else '-'


def p_expression(p):
  '''
    expression : simpleexpression
               | simpleexpression relationaloperators simpleexpression
    '''
  debug_print("expression")


def p_relationaloperators(p):
  '''
    relationaloperators : EQUAL
                        | LESSER
                        | GREATER
                        | LESSEREQUAL
                        | GREATEREQUAL
    '''
  debug_print("relationaloperators")


def p_simpleexpression(p):
  '''
    simpleexpression : term
                     | term PLUS simpleexpression
                     | term MINUS simpleexpression
                     | term OR simpleexpression
    '''
  debug_print("simpleexpression")


def p_term(p):
  '''
    term : fact
         | fact TIMES term
         | fact MINUS term
         | fact DIVIDE term
         | fact AND term
    '''
  debug_print("term")


def p_fact(p):
  '''
    fact : unaryoperator ID
         | unaryoperator LEFTPARENTHESIS expression RIGHTPARENTHESIS
         | unaryoperator INTEGER
         | unaryoperator NUMBER
         | unaryoperator STRING
         | unaryoperator BOOLEAN
    '''
  debug_print("fact")


def p_unaryoperator(p):
  '''
    unaryoperator : PLUS
                  | MINUS
                  | empty
    '''
  debug_print("unaryoperator")


def p_empty(p):
  '''
    empty :
    '''
  pass


def p_error(p):
  print("Error in line ", p.lineno)
  print("Syntax Error with", p)
