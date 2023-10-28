from ray import Ray
from vector import Vector
from point import Point
from tuple import allowed_error

class Intersection():
  # represents an intersection instance, stores t value of intersection and intersected object
  def __init__(self, t, obj):
    self.t = t
    self.obj = obj

  def hit(list):
    # return the intersection object with the lowest non-negative t value from a list of intersections
    # big potential for optimization later

    sorted_list = sorted(list, key=lambda intersection: intersection.t)
    
    for intersection in sorted_list:
      if intersection.t >= 0:
        return intersection

    return None
  
  def prepare_computations(intersect, ray):
    assert isinstance(intersect, Intersection)
    assert isinstance(ray, Ray)
    computations = Computations()
    computations.t = intersect.t
    computations.obj = intersect.obj
    computations.point = Point.to_point(ray.position(computations.t))
    computations.eyev = Vector.to_vector(-ray.direction)
    computations.normalv = computations.obj.normal_at(computations.point)
    computations.over_point = Point.to_point(computations.point + computations.normalv * allowed_error)

    if computations.normalv.dot_product(computations.eyev) < 0:
      computations.inside = True
      computations.normalv = Vector.to_vector(-computations.normalv)
    else:
      computations.inside = False

    return computations

class Computations():
  def __init__(self):
    self.t = 0
    self.obj = None
    self.point = None
    self.eyev = None
    self.normalv = None
    self.inside = False
    self.over_point = None
