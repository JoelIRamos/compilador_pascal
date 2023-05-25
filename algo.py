let = r"\[]"
num = r"\[]"
digit = r"\[]"
alfanum = r"\[]"

print("hello world")
tokens = [
  'program', 'var', 'procedure', 'begin', 'end', 'for', 'if', 'while', 'then',
  'do'
]
operadores = {'+': 'SUM', '-': 'REST', '*': 'MULTIPLICATION', '/': 'DIVISION'}

operadores_logicos = {
  '=': 'EQUAL',
  '>': 'GREATER',
  '<': 'LESSER',
  '<=': 'LESSER_EQUAL',
  '>=': 'GREATER_EQUAL',
  '!=': 'NOT_EQUAL'
}

modificadores_unitarios = {'++': 'INCREMENTER', '--': 'DEREMENTER'}

modificadores_binarios = {
  '+=': 'SUMER',
  '-=': 'SUBTRACTER',
  '*=': 'MULTIPLIER',
  '/=': 'DIVIDER',
}