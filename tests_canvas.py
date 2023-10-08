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
    c = Canvas(1,1)
    ppm = c.canvas_to_ppm_string()
    comp = "P3\n1 1\n255\n0 0 0 \n"
    self.assertEqual(ppm, comp)

  def test_ppm_line_length(self):
    # ppm line length should never exceed 70 characters
    # allow certain editors to read generated files

    c = Canvas(10, 2)
    for row in c.pixels:
      for color in row:
        color.x = 1
        color.y = 0.8
        color.z = 0.6

    ppm = c.canvas_to_ppm_string()
    comp = ("""P3\n10 2\n255
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 \n""")
    self.assertEqual(ppm, comp)
   

if __name__ == "__main__":
  unittest.main()

