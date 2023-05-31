 # ***************** MAIN.PY FUNCTIONS *****************

# Import all the text information from a file .p in the Programs Folder
def importData(file_name):
  file_name = "./Programs/" + file_name + ".p"
  try:
    with open(file_name, 'r') as file:
      data = file.read()
  except FileNotFoundError:
    print("Couldn't find the file", {file_name})
  except IOError:
    print("Couldn't open the file", {file_name})
  return data

# Print a tuple that has recursive subtuples (used for Sintactic Tree in main debug)
def print_tuple(result):
  for res in result:
    if isinstance(res,tuple):
      print_tuple(res)
    else:
      print(res)



# ***************** PARSER.PY FUNCTIONS *****************

# ------------ Parsing ------------

# Uncomment the second line for debugging purposes
def debug_print(object):
  # print(object)
  pass


# Call Function to simplify a recursive tupple so all information is plain and in a single tuple
def simplifyTuple(original_tuple):
  return tuple(simplifyTuple_aux(original_tuple))

# SimplifyTuple Auxiliar
def simplifyTuple_aux(original_tuple):
  vector = []
  if isinstance(original_tuple, tuple):
    vector.append(original_tuple[0])
    vector.extend(simplifyTuple_aux(original_tuple[1]))
  else:
    vector.append(original_tuple)
  return vector


# Separate a tuple with subtuples whenever there is a "stops"
def separateVariables(t):
  # t = flatten_tuple(t)
  sub_tuple = []
  temp = []
  stops = ['var', 'if', 'while', ':=', 'for']
  for elemento in t:
    # if elemento == 'var':
    if elemento in stops:
      if temp:
        sub_tuple.append(tuple(temp))
        temp = []
    temp.append(elemento)
  if temp:
    sub_tuple.append(tuple(temp))

  return eliminar_coma_extra(sub_tuple)

# Eliminate the Final extra comma in the tuple
def eliminar_coma_extra(tupla):
  if len(tupla) == 1 and isinstance(tupla[0], tuple):
    return tupla[0]
  else:
    return tupla



# ------------ Semantic ------------

# Check if the data types can be used together (Functions as my Semantic Cube)
def checkDataType(op1, op2):
  dataType1 = op1[1]
  dataType2 = op2[1]
  # INT, BOOL, REAL, STRING
  if (dataType1 == 'int' and dataType2 == 'int'):
    return [dataType1, dataType2]
  elif (dataType1 == 'bool' and dataType2 == 'bool'):
    return [dataType1, dataType2]
  elif (dataType1 == 'real' and dataType2 == 'real'):
    return [dataType1, dataType2]
  elif (dataType1 == 'string' and dataType2 == 'string'):
    return [dataType1, dataType2]
  elif (dataType1 == 'real' and dataType2 == 'int'):
    return [dataType1, dataType2]
  elif (dataType1 == 'int' and dataType2 == 'real'):
    return [dataType1, dataType2]
  else:
    return False




# # Function to flatten a tuple
# def flatten_tuple(tupla):
#   tuplas_combinadas = []

#   def recursive_flatten(tupla):
#     for elemento in tupla:
#       if isinstance(elemento, tuple):
#         recursive_flatten(elemento)
#       else:
#         tuplas_combinadas.append(elemento)

#   recursive_flatten(tupla)
#   return tuple(tuplas_combinadas)




