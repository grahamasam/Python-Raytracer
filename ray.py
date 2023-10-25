from point import Point
from vector import Vector

class Ray():
  def __init__(self, origin, direction):
    assert isinstance(origin, Point)
    assert isinstance(direction, Vector)
    self.origin = origin
    self.direction = direction

  def position(self, t):
    return self.origin + self.direction * t