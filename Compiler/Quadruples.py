class Quadruples():

  def __init__(self):
    self.quadruples = []
    self.counter = 0
  
  # For printing purpuses
  def __str__(self):
    return str(self.quadruples)

  # Create a new Quadruple
  def addQuadruples(self, operator, left, right, result):
    self.quadruples.append([operator, left, right, result])
    self.counter += 1

  # Fill the goTo's of a defined Quadruple
  def fillQuadruples(self, quadruple, result):
    self.quadruples[quadruple][3] = result

  # Get the current position of the Quadruples
  def getCounter(self):
    return self.couner

  # Print the quadruple in lines
  def print(self):
    line = 0;
    for quadrupe in self.quadruples:
      print(line, ".- ",quadrupe) 
      line += 1

  # write cuadruplos on file
  # def writeCuadruplos(self):
  #   with open('cuadruplos.txt', 'w') as f:
  #     for cuadruplo in self.cuadruplos:
  #       f.write(str(cuadruplo) + '\n')
