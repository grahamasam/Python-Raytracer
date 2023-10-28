from intersection import Intersection
from sphere import Sphere
from material import Material
from point import Point
from vector import Vector
from point_light import Point_Light
from canvas import Canvas
from ray import Ray
from matrix import Matrix
from scene import Scene
from camera import Camera
from color import Color
import math


class main():
  floor = Sphere()
  floor.transform_matrix = Matrix.generate_scaling(100,0.01,100)
  floor.material = Material()
  floor.material.color = Color(0.9686,0.9686,0.8824)
  floor.material.specular = 0

  middle = Sphere()
  middle.transform_matrix = Matrix.generate_translation(-0.5,1.5,3)
  #middle.transform_matrix = middle.transform_matrix * Matrix.generate_shear(0,0,1,0,2,0)
  middle.transform_matrix = middle.transform_matrix * Matrix.generate_scaling(3,3,3)
  middle.material = Material()
  middle.material.color = Color(0.9,0.6157,0.9804)
  middle.material.diffuse = 0.7
  middle.material.specular = 0.3

  small = Sphere()
  small.transform_matrix = Matrix.generate_translation(1.2,0.5,0)
  small.material = Material()
  small.material.color = Color(1,0.9294,0.4549)
  small.material.diffuse = 1
  small.material.specular = 0.5
  small.material.shininess = 400


  scene = Scene()
  scene.add_object(floor)
  scene.add_object(middle)
  scene.add_object(small)

  scene.set_light(Point_Light(Point(10,10,-3), Color(1,1,1)))

  camera = Camera(80,50,math.pi/2.5)
  camera.transform = Matrix.view_transformation(Point(0,1.5,-5),Point(0,1,0),Vector(0,1,-0.8))

  canvas = camera.render(scene)

  with open("test.ppm", "w") as img_file:
    img_file.write(canvas.canvas_to_ppm_string())


if __name__ == "__main__":
  main()