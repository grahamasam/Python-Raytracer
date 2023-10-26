from point import Point
from ray import Ray
from matrix import Matrix
from intersection import Intersection
import math

class Sphere():
  def __init__(self):
    # initialize unit sphere
    # cannot assign a sphere with different values for center and radius, we will use
    # transform matrices to resize, translate, and squeeze/stretch sphere into place.
    self.center = Point(0,0,0)
    self.radius = 1
    self.transform_matrix = Matrix.build_4_matrix((1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))

  # function to calculate a ray's intersection with a sphere. returns a list of two
  # intersection objects or an empty list if there are none. If the ray is tangent
  # to the sphere, it will return 2 intersections with the same t value.
  def intersection(self, ray):
    assert isinstance(ray, Ray)

    # transform ray by inverse of transform_matrix account for sphere transforms
    ray2 = ray.transform(self.transform_matrix.inverse())

    sphere_to_ray = ray2.origin - self.center
    a = ray2.direction.dot_product(ray2.direction)
    b = 2 * ray2.direction.dot_product(sphere_to_ray)
    c = sphere_to_ray.dot_product(sphere_to_ray) - 1

    discriminant = (b * b) - (4 * a * c) 

    if discriminant >= 0:
      i1 = Intersection((-b - math.sqrt(discriminant)) / (2 * a), self)
      i2 = Intersection((-b + math.sqrt(discriminant)) / (2 * a), self)
      
      return (i1, i2)

    return ()
  
  def set_transform(self, matrix):
    self.transform_matrix = matrix

  def normal_at(self, Point):
    pass