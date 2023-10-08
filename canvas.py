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

  def canvas_to_ppm_string(self):
    ppm = ""

    def to_byte(c):
      return round(max(min(c * 255, 255), 0))
    
    # write image header
    ppm = ("P3\n{} {}\n255\n".format(self.width, self.height))

    count = 0

    for row in self.pixels:
      count = 0
      for color in row:
          add = "{} {} {} ".format(to_byte(color.x), to_byte(color.y), to_byte(color.z))
          count += len(add)
          if count < 70:
            ppm = ppm + add
          else:
            ppm = ppm + "\n" + add
            count = len(add)
      ppm = ppm + "\n"

    return ppm
