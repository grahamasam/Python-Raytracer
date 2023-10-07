import unittest
from canvas import Canvas
from color import Color

class testCanvas(unittest.TestCase):
  def setUp(self):
    self.c = Canvas(640, 400)

  def test_write_pixel(self):
    red = Color(1,0,0)
    self.c.write_pixel(100, 125, red)
    self.assertTrue(self.c.pixel_at(100,125).equals(red))

  def test_ppm_header(self):
    c = Canvas(5,3)
    ppm = c.canvas_to_ppm_string()

if __name__ == "__main__":
  unittest.main()

