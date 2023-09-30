from tuple import Tuple

class Point(Tuple):
  # class to store points in 3 dimensional space

  def __init__(self, x=0.0, y=0.0, z=0.0):
    self.x = x
    self.y = y
    self.z = z
    self.w = 1.0