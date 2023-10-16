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
    self.three = Matrix.build_matrix(([1,2,3],[-1,-2,-3],[0,1,2]))
  
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

  def test_build_matrix(self):
    array = ([1,2,3,4],[-1,-2,-3,-4],[2,3,4,5])
    two = Matrix.build_matrix(array)
    #print(two)

  def test_submatrix(self):
    sub = self.three.submatrix(1,1)
    sub1 = self.three.submatrix(0,2)
    #print(sub)
    #print(sub1)

  def test_minor(self):
    matrix = Matrix.build_matrix(([3,5,0],[2,-1,7],[6,-1,5]))
    self.assertEqual(matrix.minor(1,0), 25)

  def test_cofactor(self):
    matrix = Matrix.build_matrix(([3,5,0],[2,-1,-7],[6,-1,5]))
    self.assertEqual(matrix.cofactor(0,0), -12)
    self.assertEqual(matrix.cofactor(1,0), -25)
    det = matrix.determinant()
    matrix2 = Matrix.build_matrix(([1,1,1,1],[0,3,5,0],[0,2,-1,-7],[0,6,-1,5]))
    self.assertEqual(matrix2.cofactor(0,0), det)

  def test_determinant(self):
    matrix = Matrix.build_matrix(([-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]))
    self.assertEqual(matrix.cofactor(0,0), 690)
    self.assertEqual(matrix.cofactor(0,1), 447)
    self.assertEqual(matrix.determinant(), -4071)

  def test_is_invertible(self):
    invertible = Matrix.build_matrix(([-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]))
    not_invertible = Matrix.build_matrix(([-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[0,0,0,0]))
    self.assertTrue(invertible.is_invertible())
    self.assertFalse(not_invertible.is_invertible())

  def test_inverse(self):
    matrix = Matrix.build_matrix(([-5,2,6,-8],[1,-5,1,8],[7,7,-6,-7],[1,-3,7,4]))

    inverse = matrix.inverse()

    self.assertEqual(matrix.determinant(), 532)
    self.assertEqual(matrix.cofactor(2,3), -160)
    self.assertEqual(inverse.get_index(3,2), -160/532)
    self.assertEqual(matrix.cofactor(3,2), 105)
    self.assertEqual(inverse.get_index(2,3), 105/532)

  def test_inverse_2(self):
    matrix = Matrix.build_matrix(([8,-5,9,2],[7,5,6,1],[-6,0,9,6],[-3,0,-9,-4]))

    inverse = matrix.inverse()

    self.assertEqual(matrix.cofactor(0,0) / matrix.determinant(), inverse.get_index(0,0))
    self.assertEqual(matrix.cofactor(1,0) / matrix.determinant(), inverse.get_index(0,1))

  def test_inverse_3(self):
    a = Matrix.build_matrix(([8,-5,9,2],[7,5,6,1],[-6,0,9,6],[-3,0,-9,-4]))
    b = Matrix.build_matrix(([-5,2,6,-8],[1,-5,1,8],[7,7,-6,-7],[1,-3,7,4]))

    c = a * b
    self.assertTrue(a.equals(c * b.inverse()))

if __name__ == "__main__":
  unittest.main()