from point import Point
from ray import Ray
from intersection import Intersection
import math

class Sphere():
  def __init__(self):
    # initialize unit sphere
    self.center = Point(0,0,0)
    self.radius = 1

  def intersection(self, ray):
    assert isinstance(ray, Ray)
    sphere_to_ray = ray.origin - self.center
    a = ray.direction.dot_product(ray.direction)
    b = 2 * ray.direction.dot_product(sphere_to_ray)
    c = sphere_to_ray.dot_product(sphere_to_ray) - 1
    #self.radius * self.radius
    discriminant = (b * b) - (4 * a * c) 

    if discriminant >= 0:
      i1 = Intersection((-b - math.sqrt(discriminant)) / (2 * a), self)
      i2 = Intersection((-b + math.sqrt(discriminant)) / (2 * a), self)
      
      return (i1, i2)

    return ()