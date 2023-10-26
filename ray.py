from point import Point
from vector import Vector
from tuple import Tuple

class Ray():
  def __init__(self, origin, direction):
    assert isinstance(origin, Point)
    assert isinstance(direction, Vector)
    self.origin = origin
    self.direction = direction

  def position(self, t):
    return self.origin + self.direction * t
  
  def transform(self, matrix):
    new_origin = matrix * self.origin
    new_dir = matrix * self.direction
    return Ray(Point(new_origin.x, new_origin.y, new_origin.z), Vector(new_dir.x, new_dir.y, new_dir.z))