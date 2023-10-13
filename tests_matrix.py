import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
  def setUp(self):
    self.m = Matrix(4,4)
    self.n = Matrix(4,4)
    self.n.set_index(0,0,1)
  
  def test_constructor(self):
    self.assertEqual(self.m.width, 4)
    self.assertEqual(self.m.height, 4)
    matrix_str = self.m.__str__()
    comp = """0 0 0 0 \n0 0 0 0 \n0 0 0 0 \n0 0 0 0 \n"""
    self.assertEqual(matrix_str, comp)

  def test_two_by_two(self):
    c = Matrix(2,2)
    self.assertEqual(c.width, 2)
    self.assertEqual(c.height, 2)

  def test_set_index(self):
    c = Matrix(2,2)
    c.set_index(0,0,3)
    c.set_index(0,1,1)
    c.set_index(1,0,12)
    c.set_index(1,1,-2)
    matrix_str = c.__str__()
    comp = "3 1 \n12 -2 \n"
    self.assertEqual(matrix_str, comp)

  def test_equals(self):
    self.assertFalse(self.m.equals(self.n))

if __name__ == "__main__":
  unittest.main()