from tuple import Tuple

class Vector(Tuple):
  # class to store vectors of 3 dimensions
  
  def __init__(self, x=0.0, y=0.0, z=0.0):
    self.x = x
    self.y = y
    self.z = z
    self.w = 0.0
  
  # cross product for 3 dimensional vectors
  def cross(self, obj):
    assert isinstance(obj, Vector)
    return Vector(self.y * obj.z - self.z * obj.y, 
                  self.z * obj.x - self.x * obj.z,
                  self.x * obj.y - self.y * obj.x )