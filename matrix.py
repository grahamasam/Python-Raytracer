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