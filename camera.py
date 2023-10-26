from ray import Ray
from intersection import Computations, Intersection
from point_light import Point_Light
from matrix import Matrix
from color import Color
from point import Point
from vector import Vector
from canvas import Canvas
from scene import Scene
import math

class Camera():
  def __init__(self, hsize, vsize, field_of_view):
    self.hsize = hsize
    self.vsize = vsize
    self.field_of_view = field_of_view
    self.transform = Matrix.build_4_matrix((1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))

    # calculate aspect ratio
    half_view = math.tan(self.field_of_view / 2)
    aspect = self.hsize / self.vsize

    if aspect >= 0:
      self.half_width = half_view
      self.half_height = half_view/aspect
    else:
      self.half_width = half_view * aspect
      self.half_height = half_view

    # calcualte pixel size
    self.pixel_size = (self.half_width * 2) / self.hsize

  def ray_for_pixel(self,px,py):
    xoffset = (px + 0.5) * self.pixel_size
    yoffset = (py + 0.5) * self.pixel_size

    world_x = self.half_width - xoffset
    world_y = self.half_height - yoffset

    pixel = self.transform.inverse() * Point(world_x,world_y,-1)
    origin = Point.to_point(self.transform.inverse() * Point(0,0,0))
    direction = Vector.to_vector((pixel - origin).normalize())

    return Ray(origin, direction)
  
  def render(self, scene):
    assert isinstance(scene, Scene)
    image = Canvas(self.hsize, self.vsize)

    for y in range(self.vsize - 1):
      for x in range(self.hsize - 1):
        ray = self.ray_for_pixel(x,y)
        color = scene.color_at(ray)
        image.write_pixel(y,x,color)

    return image