class Symbols():

  def __init__(self):
    self.symbols = {}
    self.counter = 0

  # For printing purpuses
  def __str__(self):
    return str(self.symbols)

  # Add a new Symbol
  def writeSymbol(self, id, value, datatype, position):
    self.symbols[id] = [value, datatype, position]

  # Get the data of a symbol
  def getSymbol(self, id):
    try:
      # Firt Check if it is a value and not a variable
      # If the value is either an ID or a Float (Bools can be seen as int)
      if id == None:
        return False
      if (isinstance(id, int) or isinstance(id, float)):
        # If its string form shows its a bool, return bool
        if (str(id) == 'True' or str(id) == 'False'):
          return [id, 'bool', None]
        elif (isinstance(id, int)):  # Check for INTs
          return [id, 'int', None]
        else:  # else return a real number
          return [id, 'real', None]
      # If the value is a bool
      elif (isinstance(id, bool)):
        return [id, 'bool', None]
      elif (isinstance(id, str)):
        if (id[0] == '"'):
          return [id, 'str', None]
        else:
          # If this search breaks, then it doesn't exist
          return self.symbols[id]
      else:
        print("CE: Not a valid datatype for: ", id)
        return False
    except:  # ID doesn't exist
      return False

  # Function for creating the temporal variables
  def generateTemporal(self):
    self.counter += 1
    return "T" + str(self.counter - 1)

  def print(self):
    for key, value in self.symbols.items():
      print(key, " : ", value)

  def getRealValues(self, id1, id2):
    if self.getSymbol(id1):
      id1_value = self.getSymbol(id1)[0]
    else:
      id1_value = None

    if self.getSymbol(id2):
      id2_value = self.getSymbol(id2)[0]
    else:
      id2_value = None
    return id1_value, id2_value

  def getDataTypes(self, id1, id2, id3):
    if self.getSymbol(id1):
      id1_datatype = self.getSymbol(id1)[1]
    else:
      id1_datatype = None
    if self.getSymbol(id2):
      id2_datatype = self.getSymbol(id2)[1]
    else:
      id2_datatype = None
    if self.getSymbol(id3):
      id3_datatype = self.getSymbol(id3)[1]
    else:
      id3_datatype = None

    return id1_datatype, id2_datatype, id3_datatype
