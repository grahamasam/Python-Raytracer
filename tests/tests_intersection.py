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

  def test_hit(self):
    # return hit when some intersections are negative
    i1 = Intersection(2, self.sphere)
    i2 = Intersection(6, self.sphere)
    i3 = Intersection(-2, self.sphere)
    group = (i1,i2,i3)
    i = Intersection.hit(group)
    self.assertEqual(i, i1)

    # return hit when no intersections are negative 
    i1 = Intersection(14, self.sphere)
    i2 = Intersection(7364, self.sphere)
    i3 = Intersection(87, self.sphere)
    group = (i1,i2,i3)
    i = Intersection.hit(group)
    self.assertEqual(i, i1)

    # return none when all intersections are negative
    i1 = Intersection(-14, self.sphere)
    i2 = Intersection(-100, self.sphere)
    i3 = Intersection(-12345, self.sphere)
    group = (i1,i2,i3)
    i = Intersection.hit(group)
    self.assertEqual(i, None)