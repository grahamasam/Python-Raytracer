from ray import Ray

class Scene():
  def __init__(self):
    self.objects = []
    self.light = None

  def intersect_scene(self,ray):
    assert isinstance(ray, Ray)
    intersection_list = ()

    if len(self.objects) == 0:
      return intersection_list
    
    for obj in self.objects:
      intersection_list = intersection_list + obj.intersection(ray)

    sorted_list = sorted(intersection_list, key=lambda intersection: intersection.t)

    return sorted_list
  
  def add_object(self, obj):
    self.objects.append(obj)

  def set_light(self, light):
    self.light = light