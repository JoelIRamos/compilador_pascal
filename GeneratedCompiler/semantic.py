# Initialize the symbol table and quadruples
symbol_table = {}
quadruples = []


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
