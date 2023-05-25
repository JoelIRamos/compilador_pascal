import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
  "ID", "NUMBER", "PLUS", "MINUS", "PLUSPLUS", "MINUSMINUS", "TIMES", "DIVIDE",
  "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "TIMES_ASSIGN", "DIVIDE_ASSIGN",
  "DISTINCT", "EQUAL", "LESSER", "GREATER", "LESSER_EQUAL", "GREATER_EQUAL",
  "COMMA", "DOT", "COLOM", "SEMICOLOM", "LEFT_PARENTHESIS",
  "RIGHT_PRARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET"
]

reserved_words = {
  "program": "PROGRAM",
  "var": "VAR",
  "procedure": "PROCEDURE",
  "begin": "BEGIN",
  "end": "END",
  "for": "FOR",
  "if": "IF",
  "then": "THEN",
  "else": "ELSE",
  "while": "WHILE",
  "do": "DO",
  "write": "WRITE",
  "int": "INT",
  "float": "FLOAT",
  "char": "CHAR",
  "bool": "BOOL",
}

tokens = tokens + list(reserved_words.values())

t_ignore = "\t"
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUS = r'\-'
t_MINUSMINUS = r'\-\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r':='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'\-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_DISTINCT = r'<>'
t_EQUAL = r'='
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSER_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_COMMA = r','
t_DOT = r'\.'
t_COLOM = r':'
t_SEMICOLOM = r';'
t_LEFT_PARENTHESIS = r'('
t_RIGHT_PRARENTHESIS = r'\)'
t_LEFT_BRACKET = r'\{'
t_RIGHT_BRACKE = r'\}'


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  if t.value.upper() in keywords:
    t.value = t.value.upper()
    t.type = t.value
  return t


def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_error(t):
  print("caracter ilegal '%s' " % t.value[0])
  t.lexer.sikip(1)


directorio = ''
