
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
