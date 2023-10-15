from tuple import Tuple

class Matrix():
  # class to represent matrices of different widths and heights

  def __init__(self, width=2, height=2):
    # initialize matrix of width, width and height, height with 0
    self.width = width
    self.height = height
    self.matrix = [[0 for _ in range(width)] for _ in range(height)]

  def __str__(self):
    matrix_str = ""
    for row in self.matrix:
      for value in row:
        matrix_str = matrix_str + "{} ".format(value)
      matrix_str = matrix_str + "\n"
    return matrix_str

  def set_index(self, row, col, value):
    self.matrix[row][col] = value

  def get_index(self, row, col):
    return self.matrix[row][col]
  
  def equals(self, obj):
    assert isinstance(obj, Matrix)
    assert self.width == obj.width and self.height == obj.height

    for i in range(self.height):
      for j in range(self.width):
        if (self.get_index(i,j) != obj.get_index(i,j)):
          return False
        
    return True
  
  # build_4_matrix takes an array of 16 numbers and places them in a new 4x4 matrix
  # returns the created matrix
  def build_4_matrix(array):
    assert len(array) == 16
    count = 0
    new_matrix = Matrix(4,4)

    for i in range(4):
      for j in range(4):
        new_matrix.set_index(i,j,array[count])
        count = count + 1
    
    return new_matrix
  
  # build any size matrix from given 2d array
  # returns the created matrix
  def build_matrix(array):
    # figure out asserts for this, easy to mess up, hard to notice when debugging

    new_matrix = Matrix(len(array[0]), len(array))

    new_matrix.matrix = array
    #for i in range(len(array)):
    #  for j in range(len(array[0])):
    #    new_matrix.matrix[i][j] = array[i][j]
    
    return new_matrix

  def multiply_matrix(self, obj):
    assert isinstance(obj, Matrix)
    assert self.width == obj.height
    
    product_matrix = Matrix(self.height, obj.width)

    for i in range(self.width):
      sum = 0
      for j in range(obj.height):
        index_product = self.get_index(i, j) * obj.get_index(j, i)
        sum += index_product
      
    for i in range(product_matrix.height):
      for j in range(product_matrix.width):
        sum = 0
        for x in range(self.width):
            index_product = self.get_index(i, x) * obj.get_index(x, j)
            sum += index_product
        product_matrix.set_index(i,j,sum)

    return product_matrix
  
  def multiply_tuple(self, obj):
    assert isinstance(obj, Tuple)
    assert self.width == 4

    array = [0 for i in range(4)]

    for i in range(4):
      product = self.get_index(i, 0) * obj.x + self.get_index(i, 1) * obj.y + self.get_index(i, 2) * obj.z + self.get_index(i, 3) * obj.w
      array[i] = product

    return Tuple(array[0], array[1], array[2], array[3])
  
  # operator override to multiply matrix by matrix or matrix by tuple
  def __mul__(self, obj):
    # assert obj is a tuple or Matrix
    assert isinstance(obj, (Tuple, Matrix))
    
    if (isinstance(obj, Tuple)):
      return self.multiply_tuple(obj)
    if (isinstance(obj, Matrix)):
      return self.multiply_matrix(obj)
    
  def transpose(self):
    assert(self.height == self.width)

    transpose = Matrix(self.width, self.height)
    
    for i in range(self.height):
      for j in range(self.width):
        transpose.matrix[i][j] = self.matrix[j][i]

    return transpose
  
  # functions to calculate determinant of 4x4 matrix
  
  # calculate determinant of 2x2 matrix
  def determinant_2(self):
    assert(self.height == 2)
    assert(self.width == 2)

    return self.matrix[1][1] * self.matrix[0][0] - self.matrix[1][0] * self.matrix[0][1]
  
  def determinant(self):
    assert(self.height == self.width)
    det = 0
    if (self.height == 2 and self.width == 2):
      det = self.matrix[1][1] * self.matrix[0][0] - self.matrix[1][0] * self.matrix[0][1]
    else:
      for i in range(self.width):
        det = det + self.matrix[0][i] * self.cofactor(0,i)

    return det

  
  # return submatrix of given matrix removing input row and column
  def submatrix(self, row, col):
    assert(row <= self.height - 1)
    assert(col <= self.width - 1)

    submatrix = Matrix(self.height - 1, self.width - 1)
    x = 0
    y = 0
    for i in range(self.height - 1):
      if x == row: x = x + 1
      y = 0
      for j in range(self.width - 1):
        if y == col: y = y + 1
        submatrix.matrix[i][j] = self.matrix[x][y]
        y = y + 1
      x = x + 1
      
    return submatrix
  
  # calculate minor of matrix. Minor is the determinant of submatrix removing input row and column
  def minor(self, row, col):
    assert(self.height == self.width)
    submatrix = self.submatrix(row, col)

    det = 0

    if (submatrix.height > 2):
      for i in range(submatrix.width):
        det = det + submatrix.minor(0,i)
    else:
      det = submatrix.determinant()

    return det
  
  # calculate cofactor of matrix. Cofactor is the minor from removing input row and column
  # and negated depending on its location. Formula is (-1)^(i+j) * Aij where i and j are the
  # row and column and A is the determinant of the submatrix obtained by removing ith row and
  # jth column
  def cofactor(self, row, col):
    # Check if the matrix is square
    if self.height != self.width:
        raise ValueError("Matrix must be square for cofactors.")
    submatrix = self.submatrix(row,col)
    return  (-1) ** (row + col) * submatrix.determinant()


# global identity matrices

identity_matrix_4 = Matrix.build_4_matrix((1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))