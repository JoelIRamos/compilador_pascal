import ply.lex as lex

# ----------------- TOKENS -----------------

# List of token names
tokens = [
  'ID', 
  'NUMBER', 
  'INTEGER', 
  'FLOATING', 
  'BOOLEAN', # True or False
  'CHARACTER', # 'c'
  'STRING', # "Hello World"
  'PLUS', # +
  'MINUS', # -
  'TIMES', # *
  'DIVIDE', # /
  'PLUSPLUS', # ++
  'MINUSMINUS', # --
  'ASSIGN', # :=
  'PLUSASSIGN', # +=
  'MINUSASSIGN', # -=
  'TIMESASSIGN', # *=
  'DIVIDEASSIGN', # /=
  'DISTINCT', # <>
  'EQUAL', # =
  'LESSER', # <
  'GREATER', # >
  'LESSEREQUAL', # <= 
  'GREATEREQUAL', # >=
  'COMMA', # ,
  'DOT', # .
  'COLON', # :
  'SEMICOLON', # ;
  'LEFTPARENTHESIS', # (
  'RIGHTPARENTHESIS', # )
  'LEFTBRACKET', # {
  'RIGHTBRACKET' # }
]

# List of keywords (will be added to the tokens)
keywords = {
  'program': 'PROGRAM',
  'var': 'VAR',
  'procedure': 'PROCEDURE',
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
  'float': 'FLOAT',
  'char': 'CHAR',
  'bool': 'BOOL',
}

# Adding the keywords to the tokens
tokens = tokens + list(keywords.values())



# ----------------- Regular Expresions -----------------

# Regular expression rules for simple tokens
# t_BOOLEAN = r'True|False' # True or False
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_ASSIGN = r'='
t_PLUSASSIGN = r'\+='
t_MINUSASSIGN = r'-='
t_TIMESASSIGN = r'\*='
t_DIVIDEASSIGN = r'/='
t_DISTINCT = r'<>'
t_EQUAL = r':='
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSEREQUAL = r'<='
t_GREATEREQUAL = r'>='
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'

# Regular expression for Characters
def t_CHARACTER(t): 
  r'\'.\''
  # Remove simple columns
  t.value = t.value[1]
  return t

# Regular expression for Strings
def t_STRING(t):
  r'\".*\"'
  t.value = t.value[1:-1]
  return t
  
# Regular expression for numbers
def t_NUMBER(t):
  # Catch a real number
  r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
  r'\d+'
  # If number is an integer
  if t.value.isdigit():
    t.value = int(t.value)
    t.type = "INTEGER" 
  # ToDo: Floating can be real as 10e9?
  else: # If not it is a floating point
    t.value = t.value
    t.type = "FLOATING"
  return t

# Regular expression for booleans
def t_BOOLEAN(t):
  r'True|False'
  # ToDo: True and Flase or 1 and 0
  # if (t.value == 'True'):
  #   t.value = 1
  # else: 
  #   t.value = 0
  return t

# Regular expression for ID's
# An ID must start with a char of _ and can have digits later
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  if t.value in keywords:
    t.type = t.value.upper()
  return t

# Regular expression for Comments
# ToDo: Only functions for in-line, not multi-line
# def t_COMMENT(t):
#   r'\(\*(.*?\n)\*\)'
#   pass

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


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
9.0
9045
.09
1.78
10.
1e10
e5
True False
flase true
char a :='b'
"Hello Baby "
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok)
