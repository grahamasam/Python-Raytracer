import unittest
from tuple import Tuple
from vector import Vector
from point import Point

class TestTuplePointVector(unittest.TestCase):
  def setUp(self):
    self.point1 = Tuple(4.3, -4.2, 3.1, 1.0)
    self.vector1 = Tuple(4.3, -4.2, 3.1, 0.0)
    self.point2 = Point(4.3, -4.2, 3.1)
    self.vector2 = Vector(4.3, -4.2, 3.1)

  def test_tuple_construction_point(self):
    self.assertEqual(self.point1.x, 4.3)
    self.assertEqual(self.point1.y, -4.2)
    self.assertEqual(self.point1.z, 3.1)
    self.assertEqual(self.point1.w, 1.0)
    self.assertTrue(self.point1.is_point())

  def test_tuple_construction_vector(self):
    self.assertEqual(self.vector1.x, 4.3)
    self.assertEqual(self.vector1.y, -4.2)
    self.assertEqual(self.vector1.z, 3.1)
    self.assertEqual(self.vector1.w, 0.0)
    self.assertTrue(self.vector1.is_vector())

  def test_point_constructor(self):
    self.assertTrue(self.point2.equals(self.point1))

  def test_vector_constructor(self):
    self.assertTrue(self.vector2.equals(self.vector1))

  def add_tuples(self):
    self.assertEqual(self.vector1.add(self.point1), Tuple(8.7, -8.2, 6.2, 1.0))

if __name__ == "__main__":
  unittest.main()