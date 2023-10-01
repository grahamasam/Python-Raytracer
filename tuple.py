class Tuple():
  # class to contain three data points
  # w determiner to specify data type
  # 0.0 = vector, 1.0 = point
  def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def is_vector(self):
    if (self.w == 0.0):
      return True
    return False
  
  def is_point(self):
    if (self.w == 1.0):
      return True
    return False
  
  def equals(self, tuple):
    return self.x == tuple.x and self.y == tuple.y and self.z == tuple.z and self.w == tuple.w
  
  def add(self, tuple):
    return Tuple(self.x + tuple.x, self.y + tuple.y, self.z + tuple.z, self.w + tuple.w)
  
  def subtract(self, tuple):
    return Tuple(self.x - tuple.x, self.y - tuple.y, self.z - tuple.z, self.w - tuple.w)
           
