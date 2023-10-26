import unittest
from matrix import Matrix, identity_matrix_4
from tuple import Tuple
from point import Point
from vector import Vector
from camera import Camera
import math

class TestCamera(unittest.TestCase):
  def setUp(self):
    self.c1 = Camera(200,125,math.pi/2)
    self.c2 = Camera(125,200,math.pi/2)

  def test_pixel_size_horizontal(self):
    self.assertAlmostEqual(self.c1.pixel_size,0.01)

  def test_pixel_size_vertical(self):
    self.assertAlmostEqual(self.c2.pixel_size,0.01)

  def test_ray_for_pixel_1(self):
    c = Camera(201,101,math.pi/2)
    r = c.ray_for_pixel(0,0)
    self.assertTrue(r.origin, Point(0,0,0))
    self.assertTrue(r.direction, Vector(0.66519, 0.33259, -0.66851))

  def test_ray_for_pixel_2(self):
    c = Camera(201,101,math.pi/2)
    c.transform = Matrix.generate_rotation_y(math.pi/4) * Matrix.generate_translation(0,-2,5)
    r = c.ray_for_pixel(100,50)
    self.assertTrue(r.origin.equals(Point(0,2,-5)))
    self.assertTrue(r.direction.equals(Vector(math.sqrt(2)/2,0,-math.sqrt(2)/2)))

if __name__ == "__main__":
  unittest.main()