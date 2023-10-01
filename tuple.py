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
  
  def multiply(self, scalar):
    return Tuple
  
  # dunder methods (operator overload) for basic vector operations

  def __add__(self, other):
    return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
  
  def __sub__(self, other):
    return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w + other.w)

  # function to multiply a vector by a number (vec * 3)
  def __mul__(self, num):
    # this assert will fail if num is a Tuple
    assert not isinstance(num, Tuple)
    return Tuple(self.x * num, self.y * num, self.z * num, self.w * num)
  
  # function to multiply a vector by a number (when the vector is on the right; 3 * vec)
  def __rmul__(self, num):
    return self.__mul__(num)
  
  def negate(self):
    self.x = -self.x
    self.y = -self.y
    self.z = -self.z
    self.w = -self.w
    return self