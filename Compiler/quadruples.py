class Quadruples():

  def __init__(self):
    self.quadruples = []
    self.counter = 0

  def __str__(self):
    return str(self.quadruples)

  def addQuadruples(self, operator, left, right, result):
    self.quadruples.append([operator, left, right, result])
    self.counter += 1

  def fillQuadruples(self, quadruple, result):
    self.quadruples[quadruple][3] = result

  def getCounter(self):
    return self.couner

  # write cuadruplos on file
  # def writeCuadruplos(self):
  #   with open('cuadruplos.txt', 'w') as f:
  #     for cuadruplo in self.cuadruplos:
  #       f.write(str(cuadruplo) + '\n')
