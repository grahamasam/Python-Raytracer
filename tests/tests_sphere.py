import unittest
from intersection import Intersection
from sphere import Sphere
from point import Point
from ray import Ray
from vector import Vector
from point_light import Point_Light
from color import Color
from material import Material
from scene import Scene
from camera import Camera
from matrix import Matrix, identity_matrix_4
import math

class testSphere(unittest.TestCase):
  def setUp(self):
    self.sphere = Sphere()
    light = Point_Light(Point(-10,10,-10), Color(1,1,1))
    s1 = Sphere()
    s1.material = Material()
    s1.material.color = Color(0.8,1.0,0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.transform_matrix = Matrix.generate_scaling(0.5,0.5,0.5)
    self.scene = Scene()
    self.scene.light = light
    self.scene.add_object(s1)
    self.scene.add_object(s2)

  def test_default_transform(self):
    self.assertTrue(self.sphere.transform_matrix.equals(identity_matrix_4))

  def test_change_transform(self):
    translate = Matrix.generate_translation(4,5,6)
    self.sphere.set_transform(translate)
    self.assertTrue(self.sphere.transform_matrix.equals(translate))

  def test_intersect_scaled(self):
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    s = Sphere()
    s.set_transform(Matrix.generate_scaling(2,2,2))
    intersects = s.intersection(r)
    self.assertEqual(len(intersects), 2)
    self.assertEqual(intersects[0].t, 3)
    self.assertEqual(intersects[1].t, 7)

  def test_intersect_translated(self):
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    s = Sphere()
    s.set_transform(Matrix.generate_translation(5,0,0))
    intersects = s.intersection(r)
    self.assertEqual(len(intersects), 0)

  def test_normal_at_translated(self):
    s = Sphere()
    s.set_transform(Matrix.generate_translation(0,1,0))
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    self.assertTrue(n.equals(Vector(0, 0.70711, -0.70711)))

  def test_scene(self):
    light = Point_Light(Point(-10,10,-10), Color(1,1,1))
    s1 = Sphere()
    s1.material = Material()
    s1.material.color = Color(0.8,1.0,0.6)
    s2 = Sphere()
    s2.transform_matrix = Matrix.generate_scaling(0.5,0.5,0.5)
    scene = Scene()
    scene.light = light
    scene.add_object(s1)
    scene.add_object(s2)
    self.assertEqual(scene.objects[0], s1)

  def test_scene_intersects(self):
    light = Point_Light(Point(-10,10,-10), Color(1,1,1))
    s1 = Sphere()
    s1.material = Material()
    s1.material.color = Color(0.8,1.0,0.6)
    s2 = Sphere()
    s2.transform_matrix = Matrix.generate_scaling(0.5,0.5,0.5)
    scene = Scene()
    scene.light = light
    scene.add_object(s1)
    scene.add_object(s2)
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    intersects = scene.intersect_scene(r)
    self.assertTrue(len(intersects), 4)
    self.assertEqual(intersects[0].t, 4)
    self.assertEqual(intersects[1].t, 4.5)

  def test_color_at(self):
    r = Ray(Point(0,0,-5), Vector(0,1,0))
    c = self.scene.color_at(r)
    self.assertTrue(c.equals(Color(0,0,0)))

  def test_color_at_hit(self):
    r = Ray(Point(0,0,-5), Vector(0,0,1))
    c = self.scene.color_at(r)
    self.assertTrue(c.equals(Color(0.38066, 0.47583, 0.2855)))

  def test_render_world(self):
    c = Camera(11,11,math.pi/2)
    at = Point(0,0,-5)
    to = Point(0,0,0)
    up = Vector(0,1,0)
    c.transform = Matrix.view_transformation(at,to,up)
    image = c.render(self.scene)
    self.assertTrue(image.pixel_at(5,5).equals(Color(0.38066, 0.47583, 0.2855)))

if __name__ == "__main__":
  unittest.main()