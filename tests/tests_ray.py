import unittest
from ray import Ray
from point import Point
from vector import Vector
from sphere import Sphere
from matrix import Matrix

class TestMatrix(unittest.TestCase):
  def setUp(self):
    self.ray1 = Ray(Point(0,0,0), Vector(1,1,1))

  def test_ray_position(self):
    self.assertTrue(self.ray1.position(3).equals(Point(3,3,3)))
    self.assertTrue(self.ray1.position(-1).equals(Point(-1,-1,-1)))

  def test_sphere_intersection(self):
    ray = Ray(Point(0,0,-5), Vector(0,0,1))
    sphere = Sphere()
    intersection = sphere.intersection(ray)
    self.assertEqual(intersection[0].t, 4.0)
    self.assertEqual(intersection[1].t, 6.0)

    # ray is tangent to sphere
    ray = Ray(Point(0,1,-5), Vector(0,0,1))
    sphere = Sphere()
    intersection = sphere.intersection(ray)
    self.assertEqual(intersection[0].t, 5.0)
    self.assertEqual(intersection[1].t, 5.0)

    # ray misses sphere
    ray = Ray(Point(0,2,-5), Vector(0,0,1))
    sphere = Sphere()
    intersection = sphere.intersection(ray)
    self.assertEqual(len(intersection), 0)

    # ray origin inside sphere (should still return 2 intersections)
    ray = Ray(Point(0,0,0), Vector(0,0,1))
    sphere = Sphere()
    intersection = sphere.intersection(ray)
    self.assertEqual(intersection[0].t, -1)
    self.assertEqual(intersection[1].t, 1)

    # sphere behind ray (should still return 2 intersections)
    ray = Ray(Point(0,0,5), Vector(0,0,1))
    sphere = Sphere()
    intersection = sphere.intersection(ray)
    self.assertEqual(intersection[0].t, -6)
    self.assertEqual(intersection[1].t, -4)
    self.assertEqual(intersection[0].obj, sphere)

  def test_translate_ray(self):
    ray = Ray(Point(1,5,6), Vector(1,0,1))
    m = Matrix.generate_translation(1,2,3)
    r = ray.transform(m)
    self.assertTrue(r.origin.equals(Point(2,7,9)))
    self.assertTrue(r.direction.equals(Vector(1,0,1)))

  def test_scale_ray(self):
    ray = Ray(Point(1,5,6), Vector(1,0,1))
    m = Matrix.generate_scaling(2,2,3)
    r = ray.transform(m)
    self.assertTrue(r.origin.equals(Point(2,10,18)))
    self.assertTrue(r.direction.equals(Vector(2,0,3)))


if __name__ == "__main__":
  unittest.main()