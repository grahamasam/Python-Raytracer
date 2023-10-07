from color import Color

class Canvas():
  # class to store information about the screen we are drawing to
  
  def __init__(self, width=0.0, height=0.0):
    self.width = width
    self.height = height
    # _ signifies we are not interested in the value of the iterator,
    # only that the number of iterations is width and height
    self.pixels = [[Color(0,0,0) for _ in range(width)] for _ in range(height)]

  def write_pixel(self, x, y, color):
    self.pixels[x][y] = color

  def pixel_at(self, x, y):
    return self.pixels[x][y]

