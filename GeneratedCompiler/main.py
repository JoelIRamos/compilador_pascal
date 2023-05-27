import ply.lex as lex
import ply.yacc as yacc

# ----------------- TOKENS -----------------

# List of token names
tokens = [
  'ID', 'NUMBER', 'INTEGER', 'BOOLEAN', 'STRING', 'PLUS', 'MINUS', 'TIMES',
  'DIVIDE', 'PLUSPLUS', 'MINUSMINUS', 'ASSIGN', 'EQUAL', 'LESSER', 'GREATER',
  'LESSEREQUAL', 'GREATEREQUAL', 'COMMA', 'COLON', 'SEMICOLON',
  'LEFTPARENTHESIS', 'RIGHTPARENTHESIS', 'LEFTBRACKET', 'RIGHTBRACKET'
]

# List of keywords (will be added to the tokens)
keywords = {
  'program': 'PROGRAM',
  'var': 'VAR',
  'begin': 'BEGIN',
  'end': 'END',
  'for': 'FOR',
  'if': 'IF',
  'then': 'THEN',
  'else': 'ELSE',
  'while': 'WHILE',
  'do': 'DO',
  'write': 'WRITE',
  'int': 'INT',
  'real': 'REAL',
  'str': 'STR',
  'bool': 'BOOL',
  'and': 'AND',
  'or': 'OR'
}

# Adding the keywords to the tokens
tokens = tokens + list(keywords.values())

# ----------------- Regular Expresions -----------------

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_ASSIGN = r':='
t_EQUAL = r'='
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSEREQUAL = r'<='
t_GREATEREQUAL = r'>='
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'


# Regular expression for Strings
def t_STRING(t):
  r'\".*\"'
  t.value = t.value[1:-1]
  return t


# Regular expression for numbers
def t_NUMBER(t):
  r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
  if '.' in t.value:
    t.value = float(t.value)
  else:
    t.value = int(t.value)
  return t


# Regular expression for booleans
def t_BOOLEAN(t):
  r'True|False'
  t.value = bool(t.value)
  return t


# Regular expression for ID's
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  if t.value in keywords:
    t.type = t.value.upper()
  return t


# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# String containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# ----------------- Parser -----------------

# Precedence of each token
precedence = (
  ('right', 'ASSIGN'),
  ('left', 'AND', 'OR'),
  ('left', 'DISTINCT', 'EQUAL'),
  ('left', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  ('left', 'PLUSPLUS', 'MINUSMINUS'),
  ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)

# Symbol table
symbol_table = {}


# Generate a new temporary variable
def new_temp():
  count = len(symbol_table) + 1
  return f"t{count}"


# Generate a new quadruple
def gen_quad(op, arg1, arg2, result):
  quad = (op, arg1, arg2, result)
  quadruples.append(quad)


# Generate a new quadruple with a jump label
def gen_quad_jump(op, arg1, arg2, result):
  quad = (op, arg1, arg2, result)
  quadruples.append(quad)
  return len(quadruples) - 1


# Backpatch a quadruple with the jump target
def backpatch(quad_index, target):
  quadruples[quad_index] = list(quadruples[quad_index])
  quadruples[quad_index][-1] = target
  quadruples[quad_index] = tuple(quadruples[quad_index])


# Generate a new quadruple with a placeholder for the jump target
def gen_quad_placeholder(op, arg1, arg2):
  quad = (op, arg1, arg2, None)
  quadruples.append(quad)
  return len(quadruples) - 1


# ----------------- Grammar Rules -----------------


def p_program(p):
  '''
    Program : PROGRAM ID LEFTBRACKET variable block RIGHTBRACKET
    '''
  print("program")


def p_variable(p):
  '''
    variable : VAR ID variables COLON datatype SEMICOLON variable
             | empty
    '''
  print("variable")


def p_variables(p):
  '''
    variables : COMMA ID variables
              | empty
    '''
  print("variables")


def p_datatype(p):
  '''
    datatype : INT
             | REAL
             | BOOL
             | STR
    '''
  print("datatype")


def p_block(p):
  '''
    block : BEGIN SEMICOLON statement END SEMICOLON
    '''
  print("block")


def p_statement(p):
  '''
    statement : writestatement statement
              | assignstatement statement
              | ifstatement statement
              | whileloop statement
              | forloop statement
              | empty
    '''
  print("statement")


def p_writestatement(p):
  '''
    writestatement : WRITE LEFTPARENTHESIS expression RIGHTPARENTHESIS SEMICOLON
    '''
  print("writestatement")


def p_assignstatement(p):
  '''
    assignstatement : ID ASSIGN expression SEMICOLON
    '''
  print("assignstatement")
  gen_quad('=', p[3], None, p[1])


def p_ifstatement(p):
  '''
    ifstatement : IF LEFTPARENTHESIS expression RIGHTPARENTHESIS THEN LEFTBRACKET statement RIGHTBRACKET elsestatement
    '''
  print("ifstatement")
  if p[3]:
    quad_index = gen_quad_jump('if', p[3], None, None)
    backpatch(quad_index, len(quadruples))
    p[7]
  else:
    quad_index = gen_quad_placeholder('if', p[3], None)
    p[7]
    jump_index = gen_quad_jump('goto', None, None, None)
    backpatch(quad_index, len(quadruples))
    backpatch(jump_index, len(quadruples))


def p_elsestatement(p):
  '''
    elsestatement : ELSE LEFTBRACKET statement RIGHTBRACKET
                  | empty
    '''
  print("elsestatement")
  if p[1] is not None:
    p[3]


def p_whileloop(p):
  '''
    whileloop : WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS DO LEFTBRACKET statement RIGHTBRACKET
    '''
  print("whileloop")
  quad_index = len(quadruples)
  if p[3]:
    quad_index = gen_quad_jump('while', p[3], None, None)
    backpatch(quad_index, len(quadruples))
    p[7]
    gen_quad_jump('goto', None, None, quad_index)


def p_forloop(p):
  '''
    forloop : FOR LEFTPARENTHESIS ID ASSIGN expression SEMICOLON expression SEMICOLON formodifier RIGHTPARENTHESIS LEFTBRACKET statement RIGHTBRACKET
    '''
  print("forloop")
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
  print("formodifier")
  p[0] = '+' if p[2] == '++' else '-'


def p_expression(p):
  '''
    expression : simpleexpression
               | simpleexpression relationaloperators simpleexpression
    '''
  print("expression")


def p_relationaloperators(p):
  '''
    relationaloperators : EQUAL
                        | LESSER
                        | GREATER
                        | LESSEREQUAL
                        | GREATEREQUAL
    '''
  print("relationaloperators")


def p_simpleexpression(p):
  '''
    simpleexpression : term
                     | term PLUS simpleexpression
                     | term MINUS simpleexpression
                     | term OR simpleexpression
    '''
  print("simpleexpression")


def p_term(p):
  '''
    term : fact
         | fact TIMES term
         | fact MINUS term
         | fact DIVIDE term
         | fact AND term
    '''
  print("term")


def p_fact(p):
  '''
    fact : unaryoperator ID
         | unaryoperator LEFTPARENTHESIS expression RIGHTPARENTHESIS
         | unaryoperator INTEGER
         | unaryoperator NUMBER
         | unaryoperator STRING
         | unaryoperator BOOLEAN
    '''
  print("fact")


def p_unaryoperator(p):
  '''
    unaryoperator : PLUS
                  | MINUS
                  | empty
    '''
  print("unaryoperator")


def p_empty(p):
  '''
    empty :
    '''
  pass


def p_error(p):
  print("Error in line ", p.lineno)
  print("Syntax Error with", p)


# ----------------- Lexer and Parser Initialization -----------------

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# ----------------- Testing -----------------

code = '''
program test {
    var x, y : int;
    var z : real;
    
    x := 5;
    y := 2;
    z := 3.14;
    
    write(x + y);
    write(x * z);
    
    if (x > y) then {
        write("x is greater than y");
    } else {
        write("x is not greater than y");
    }
    
    while (x > 0) do {
        write(x);
        x := x - 1;
    }
    
    for (i := 1; i <= 10; i++) {
        write(i);
    }
}
'''

# Initialize the symbol table and quadruples
symbol_table = {}
quadruples = []

# Parse the code
parser.parse(code, lexer=lexer)
