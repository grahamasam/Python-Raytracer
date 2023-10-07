from tuple import Tuple

class Color(Tuple):
  # class to store rgb colors

  def __init__(self, r=0.0, g=0.0, b=0.0):
    self.x = r
    self.y = g
    self.z = b
    self.w = 0

  def multiply(self, obj):
    return Color(self.x * obj.x, self.y * obj.y, self.z * obj.z)
  
  