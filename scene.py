from ray import Ray
from intersection import Computations, Intersection
from point_light import Point_Light
from color import Color

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

  def shade_hit(self, comps):
    assert isinstance(comps, Computations)
    return Point_Light.lighting(comps.obj.material, self.light, comps.point, comps.eyev, comps.normalv)
  
  def color_at(self, ray):
    intersect_list = self.intersect_scene(ray)
    hit = Intersection.hit(intersect_list)
    if hit is None:
      return Color(0,0,0)
    else:
      comps = Intersection.prepare_computations(hit, ray)
      return self.shade_hit(comps)


