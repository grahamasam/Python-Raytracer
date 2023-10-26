from tuple import Tuple

class Color(Tuple):
  # class to store rgb colors

  def __init__(self, r=0.0, g=0.0, b=0.0):
    self.x = r
    self.y = g
    self.z = b
    self.w = 0

  # override Tuple operator overloads to assert they are a color
  def __add__(self, other):
    assert isinstance(other, Color)
    return Color(self.x + other.x, self.y + other.y, self.z + other.z)
  
  def __sub__(self, other):
    assert isinstance(other, Color)
    return Color(self.x - other.x, self.y - other.y, self.z - other.z)
  
  def multiply(self, obj):
    assert isinstance(obj, Color)
    return Color(self.x * obj.x, self.y * obj.y, self.z * obj.z)
  
  

  
  