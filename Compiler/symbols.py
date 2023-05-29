class Symbols():

  def __init__(self):
    self.symbols = {}
    self.counter = 0

  def __str__(self):
    return str(self.symbols)

  def writeSymbol(self, id, value, datatype, position):
    self.symbols[id] = [value, datatype, position]

  def getSymbol(self, id):
    return self.symbols[id]

  def generateTemporal(self):
    return "T" + str(self.counter)


