import unittest
from intersection import Intersection
from sphere import Sphere

class testIntersection(unittest.TestCase):
  def setUp(self):
    self.sphere = Sphere()
    self.intersection = Intersection(5, self.sphere)

  def test_group_intersections(self):
    i1 = Intersection(2, self.sphere)
    i2 = Intersection(6, self.sphere)
    group = (i1,i2)
    self.assertEqual(group[0].t, 2)
    self.assertEqual(group[1].t, 6)
    