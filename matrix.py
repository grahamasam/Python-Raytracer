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
  
