# from Node impor node 

def importData(file_name):
  file_name = "./Programs/" + file_name + ".p"
  try:
    with open(file_name, 'r') as file:
      data = file.read()
      # print(data)
  except FileNotFoundError:
    print("Couldn't find the file", {file_name})
  except IOError:
    print("Couldn't open the file", {file_name})
  return data


def debugPrint(object):
  # print(object)
  pass


def simplifyTuple(original_tuple):
  return tuple(simplifyTuple_aux(original_tuple))


def simplifyTuple_aux(original_tuple):
  vector = []
  if isinstance(original_tuple, tuple):
    vector.append(original_tuple[0])
    vector.extend(simplifyTuple_aux(original_tuple[1]))
  else:
    vector.append(original_tuple)
  return vector


def flatten_tuple(tupla):
  tuplas_combinadas = []

  def recursive_flatten(tupla):
    for elemento in tupla:
      if isinstance(elemento, tuple):
        recursive_flatten(elemento)
      else:
        tuplas_combinadas.append(elemento)

  recursive_flatten(tupla)
  return tuple(tuplas_combinadas)

def eliminar_coma_extra(tupla):
  if len(tupla) == 1 and isinstance(tupla[0], tuple):
    return tupla[0]
  else:
    return tupla

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


def print_tuple(result):
  for res in result:
    if isinstance(res,tuple):
      print_tuple(res)
    else:
      print(res)