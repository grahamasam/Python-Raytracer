from point import Point
from color import Color
from material import Material
from vector import Vector
import math

class Point_Light():
  # a light defined by its intensity and position in space

  def __init__(self, position, intensity):
    assert isinstance(position, Point)
    assert isinstance(intensity, Color)

    self.position = position
    self.intensity = intensity

  def lighting(m, light, point, eyev, normalv):
    assert isinstance(m, Material)
    assert isinstance(light, Point_Light)
    assert isinstance(point, Point)
    assert isinstance(eyev, Vector)
    assert isinstance(normalv, Vector)

    effective_color = m.color.multiply(light.intensity)

    lightv = (light.position - point).normalize()

    ambient = effective_color * m.ambient

    light_dot_normal = lightv.dot_product(normalv)

    if light_dot_normal < 0:
      diffuse = Color(0,0,0)
      specular = Color(0,0,0)

    else:
      diffuse = effective_color * m.diffuse * light_dot_normal

      reflectv = Vector.to_vector((-lightv))
      reflectv = reflectv.reflect(normalv)
      reflect_dot_eye = reflectv.dot_product(eyev)

      if reflect_dot_eye <= 0:
        specular = Color(0,0,0)
      
      else:
        factor = math.pow(reflect_dot_eye, m.shininess)
        specular = light.intensity * m.specular * factor

    return ambient + diffuse + specular

    