import ply.yacc as yacc
from Lexer import tokens

from functions import debugPrint as debug_print

# Precedencia de cada token, var, program, id, etc.
precendence = (
  ('right',
   'ASSIGN'),  # 'PLUSASSIGN', 'MINUSASSIGN', 'TIMESASSIGN', 'DIVIDEASSIGN'
  ('left', 'AND', 'OR'),
  ('left', 'DISTINCT', 'EQUAL'),
  ('left', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),  #nonassoc
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  ('left', 'PLUSPLUS', 'MINUSMINUS'),
  ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)


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
  # TODO DONDE VA EL COLON?
  '''
  assignstatement : ID ASSIGN expression SEMICOLON
  '''
  debug_print("assignstatement")


def p_ifstatement(p):
  '''
  ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS THEN LEFTBRACKET statement RIGHTBRACKET elsestatement
  '''
  debug_print("ifstatement")


def p_elsestatement(p):
  '''
  elsestatement : ELSE LEFTBRACKET statement RIGHTBRACKET
                | empty
  '''
  debug_print("elsestatement")


def p_whileloop(p):
  '''
  whileloop : WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS DO LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("whileloop")


def p_forloop(p):
  '''
  forloop : FOR LEFTPARENTHESIS ID ASSIGN expression SEMICOLON expression SEMICOLON formodifier RIGHTPARENTHESIS LEFTBRACKET statement RIGHTBRACKET
  '''
  debug_print("forloop")


def p_formodifier(p):
  '''
  formodifier : ID PLUSPLUS
              | ID MINUSMINUS
  '''
  debug_print("formodifier")


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
  # TODO: Select DataTypes to use
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
  # p[0] = None
  debug_print("empty")
  pass


def p_error(p):
  print("Error in line ", p.lineno)
  print("Sintaxis Error with", p)


# def p_modifier(p):
#   '''modifier = formodifier SEMICOLON
#               | ID PLUSASSIGN INTEGER SEMICOLON
#               | ID MINUSASSIGN INTEGER SEMICOLON
#               | ID TIMESASSIGN INTEGER SEMICOLON
#               | ID DIVIDEASSIGN INTEGER SEMICOLON'''
