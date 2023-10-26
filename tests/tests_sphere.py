import unittest
from intersection import Intersection
from sphere import Sphere
from point import Point
from ray import Ray
from vector import Vector
from matrix import Matrix, identity_matrix_4

class testSphere(unittest.TestCase):
  def setUp(self):
    self.sphere = Sphere()

  def test_default_transform(self):
    self.assertTrue(self.sphere.transform_matrix.equals(identity_matrix_4))

  def test_change_transform(self):
    translate = Matrix.generate_translation(4,5,6)
    self.sphere.set_transform(translate)
    self.assertTrue(self.sphere.transform_matrix.equals(translate))

  def test_intersect_scaled(self):
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    s = Sphere()
    s.set_transform(Matrix.generate_scaling(2,2,2))
    intersects = s.intersection(r)
    self.assertEqual(len(intersects), 2)
    self.assertEqual(intersects[0].t, 3)
    self.assertEqual(intersects[1].t, 7)

  def test_intersect_translated(self):
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    s = Sphere()
    s.set_transform(Matrix.generate_translation(5,0,0))
    intersects = s.intersection(r)
    self.assertEqual(len(intersects), 0)


if __name__ == "__main__":
  unittest.main()