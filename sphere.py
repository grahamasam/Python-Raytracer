from point import Point
from ray import Ray
from matrix import Matrix
from intersection import Intersection
from material import Material
from vector import Vector
import math

class Sphere():
  def __init__(self):
    # initialize unit sphere with default material
    # cannot assign a sphere with different values for center and radius, we will use
    # transform matrices to resize, translate, and squeeze/stretch sphere into place.
    self.center = Point(0,0,0)
    self.radius = 1
    self.transform_matrix = Matrix.build_4_matrix((1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))
    self.material = Material()

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

  def normal_at(self, w_point):
    assert isinstance(w_point, Point)
    o_point = self.transform_matrix.inverse() * w_point
    #o_normal = o_point - Point(0,0,0)

    w_normal = self.transform_matrix.inverse().transpose() * o_point
    w_normal.w = 0

    return Vector.to_vector(w_normal.normalize())
  
  def set_material(self, m):
    assert isinstance(m, Material)

    self.material = m