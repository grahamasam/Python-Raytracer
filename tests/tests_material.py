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
    result = Point_Light.lighting(self.m,light,self.position,eyev,normalv)

    self.assertTrue(result.equals(Color(1.6364, 1.6364, 1.6364)))


if __name__ == "__main__":
  unittest.main()