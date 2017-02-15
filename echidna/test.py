from random import random
from pybrain.structure.evolvables.evolvable import Evolvable
from pybrain.optimization import HillClimber

class SimpleEvo(Evolvable):

  def __init__(self, x):
    self.x = max(0, min(x, 20))

  def mutate(self):
    self.x = max(0, min(self.x + random() - 0.3, 20))

  def copy(self):
    return SimpleEvo(self.x)

  def randomize(self):
    self.x = 20 * random()

  def __repr__(self):
    return '<-%.2f->'%(self.x)


if __name__ == "__main__":
  x0 = SimpleEvo(1.2)
  l = HillClimber(lambda x: x.x, x0, maxEvaluations = 500)
  result = l.learn()
  print result
