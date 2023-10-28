import unittest
from intersection import Intersection
from sphere import Sphere
from material import Material
from point import Point
from vector import Vector
from point_light import Point_Light
from color import Color
import math

class testMaterial(unittest.TestCase):
  def setUp(self):
    self.m = Material()
    self.position = Point(0,0,0)

  def test_lighting(self):
    eyev = Vector(0, -math.sqrt(2)/2, -math.sqrt(2)/2)
    normalv = Vector(0,0,-1)
    light = Point_Light(Point(0,10,-10), Color(1,1,1))
    in_shadow = False
    result = Point_Light.lighting(self.m,light,self.position,eyev,normalv,in_shadow)

    self.assertTrue(result.equals(Color(1.6364, 1.6364, 1.6364)))

  def test_lighting_with_shadow_surface(self):
    eyev = Vector(0,0,-1)
    normalv = Vector(0,0,-1)
    light = Point_Light(Point(0,0,-10), Color(1,1,1))
    in_shadow = True
    result = Point_Light.lighting(self.m, light, self.position, eyev, normalv, in_shadow)
    self.assertTrue(result.equals(Color(0.1,0.1,0.1)))


if __name__ == "__main__":
  unittest.main()