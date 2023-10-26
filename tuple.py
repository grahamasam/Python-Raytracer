import math

class Tuple():
  # class to contain three data points
  # w determiner to specify data type
  # 0.0 = vector, 1.0 = point
  def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def __str__(self):
    return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

  def is_vector(self):
    if (self.w == 0.0):
      return True
    return False
  
  def is_point(self):
    if (self.w == 1.0):
      return True
    return False
  
  def equals(self, tuple):
    return abs(self.x - tuple.x) <= allowed_error and \
           abs(self.y - tuple.y) <= allowed_error and \
           abs(self.z - tuple.z) <= allowed_error and \
           abs(self.w - tuple.w) <= allowed_error
  
  def add(self, tuple):
    return Tuple(self.x + tuple.x, self.y + tuple.y, self.z + tuple.z, self.w + tuple.w)
  
  def subtract(self, tuple):
    return Tuple(self.x - tuple.x, self.y - tuple.y, self.z - tuple.z, self.w - tuple.w)
  
  def multiply(self, scalar):
    return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
  
  # dunder methods (operator overload) for basic vector operations

  def __add__(self, other):
    return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
  
  def __sub__(self, other):
    return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

  # override unary minus operator for -vector negation
  def __neg__(self):
    return Tuple(-self.x, -self.y, -self.z, -self.w)
  
  # function to multiply a vector by a number (vec * 3)
  def __mul__(self, num):
    # this assert will fail if num is a Tuple
    assert not isinstance(num, Tuple)
    return Tuple(self.x * num, self.y * num, self.z * num, self.w * num)
  
  # function to multiply a vector by a number (when the vector is on the right; 3 * vec)
  def __rmul__(self, num):
    return self.__mul__(num)

  # in Python3, A / B calls A.__truediv__()
  # we need a __truediv__() method for our vector operations
  def __truediv__(self, num):
    assert not isinstance(num, Tuple)
    return Tuple(self.x / num, self.y / num, self.z / num)
  
  def dot_product(self, obj):
    return self.x * obj.x + self.y * obj.y + self.z * obj.z + self.w * obj.w
  
  def magnitude(self):
    return math.sqrt(self.dot_product(self))
  
  def normalize(self):
    return self / self.magnitude()

 # allowed error for floating point impercision
allowed_error = 0.000001