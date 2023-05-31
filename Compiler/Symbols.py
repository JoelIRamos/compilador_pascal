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
      if (isinstance(id, int) or isinstance(id, float)):
        if (str(id) == 'True' or str(id) == 'False'):
          return [id, 'bool', None]
        else:
          return [id, 'real', None]
      elif (isinstance(id, bool)):
        return [id, 'bool', None]
      else:
        return self.symbols[id]
    except:
      return False

  # Function for creating the temporal variables
  def generateTemporal(self):
    self.counter += 1
    return "T" + str(self.counter-1)
    


 