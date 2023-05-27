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


def debugPrint(t):
  print(t)
  pass
