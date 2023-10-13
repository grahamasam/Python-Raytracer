import unittest
from matrix import Matrix, identity_matrix_4
from tuple import Tuple

class TestMatrix(unittest.TestCase):
  def setUp(self):
    self.m = Matrix(4,4)
    self.n = Matrix(4,4)
    self.n.set_index(0,0,1)
    self.a = Matrix.build_4_matrix((1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2))
    self.b = Matrix.build_4_matrix((-2,1,2,3,3,2,1,-1,4,3,6,5,1,2,7,8))
  
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

  def test_build_4_matrix(self):
    array = ( 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7 )
    matrix = Matrix.build_4_matrix(array)
    #print(matrix)

  def test_matrix_multiply(self):
     c = Matrix.build_4_matrix((20,22,50,48,44,54,114,108,40,58,110,102,16,26,46,42))
     self.assertTrue(self.a.multiply_matrix(self.b).equals(c))
  
  def test_matrix_multiply(self):
     c = Matrix.build_4_matrix((20,22,50,48,44,54,114,108,40,58,110,102,16,26,46,42))
     self.assertTrue((self.a * self.b).equals(c))

  def test_multiply_tuple(self):
    tuple = Tuple(1,2,3,4)
    c = Matrix.build_4_matrix((1,1,1,1,2,2,2,2,1,1,1,1,1,0,0,0))
    self.assertTrue((c * tuple).equals(Tuple(10,20,10,1)))

  def test_identity_matrix_4(self):
    self.assertTrue((self.a * identity_matrix_4).equals(self.a))

  def test_transpose(self):
    transpose = Matrix.build_4_matrix((-2,3,4,1,1,2,3,2,2,1,6,7,3,-1,5,8))
    self.assertTrue(self.b.transpose().equals(transpose))

  def test_transpose_identity(self):
    self.assertTrue(identity_matrix_4.transpose().equals(identity_matrix_4))

if __name__ == "__main__":
  unittest.main()