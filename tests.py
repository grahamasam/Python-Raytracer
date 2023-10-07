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
    self.a = Tuple(1, 2, 3, 4)
    self.b = Tuple(4, 3, 2, 1)
    self.c = Tuple(1, 0, 0, 0)

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

  def test_add_tuples(self):
    self.assertTrue(self.vector1.add(self.point1).equals(Tuple(8.6, -8.4, 6.2, 1.0)))

  def test_subtract_tuples(self):
    self.assertTrue(self.point2.subtract(self.vector2).equals(Tuple(w=1.0)))

  def test_mul_operator(self):
    self.assertTrue((self.a * 2).equals(Tuple(2, 4, 6, 8)))

  def test_rmul_operator(self):
    self.assertTrue((2 * self.a).equals(Tuple(2, 4, 6, 8)))

  def test_neg_opeartor(self):
    self.assertTrue((-Tuple(1,2,3,4)).equals(Tuple(-1,-2,-3,-4)))

  def test_dot_prodcut(self):
    self.assertEqual(self.a.dot_product(self.b), 20)

  def test_magnitude(self):
    self.assertEqual(self.c.magnitude(), 1)

  def test_normalize(self):
    self.assertEqual(self.vector1.normalize().magnitude(), 1)

if __name__ == "__main__":
  unittest.main()