import ply.lex as lex

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