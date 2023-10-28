# Python-Raytracer
This project is a raytracer implemented using only Python default libraries.


An example main method is included to render the following scene. 

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9417a08d-c806-46d9-b7d4-6382a476aed3)

Objects in the scene can be translated, scaled, and sheared.

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/c16d4a55-c43f-4feb-8009-4a4796087bd5)

Matrices generated using the matrix class's 'generate_' functions can be multiplied with a scene object's transform matrix to change their appearance. When initialized, all sphere objects are unit spheres (center at (0,0,0) with radius 1). So, translations will initially move a sphere from the origin and scaling/shearing will initially alter a sphere of radius 1.
```
  middle = Sphere()
  middle.transform_matrix = Matrix.generate_translation(-0.5,1.5,3)
  middle.transform_matrix = middle.transform_matrix * Matrix.generate_shear(0,0,1,0,1,0)
  middle.transform_matrix = middle.transform_matrix * Matrix.generate_scaling(3,3,3)
```

The material of an object can be changed to alter how it is shaded. 

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/52188a25-d1cb-4488-8e01-d14e10285725)

A material object is initialized with 5 parameters. Color represents the base color of the material and ambient, diffuse, specular, and shininess affect how the material is shaded based on the [Phong model of specular reflection](https://en.wikipedia.org/wiki/Phong_reflection_model). 
```
class Material():
  def __init__(self, color=Color(1,1,1), ambient=0.1, diffuse=0.9, specular=0.9, shininess=200.0):
```

The camera is maneuverable to view the scene from different perspectives and angles.

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9f284e0f-280f-4157-8798-f22d552aec25)

To change the viewing angle, reference the following lines in main.py. This creates a camera object and sets the resolution of the image to 566 by 350 pixels with a field of view of pi/2.5. The second line sets the camera's transformation matrix to a view transformation matrix representing a vector pointing from a point (0,1.5,-5) to (0,1,0) with "up" being the vector <0,1,-0.8> relative to the forward direction.
```
  camera = Camera(566,350,math.pi/2.5)
  camera.transform = Matrix.view_transformation(Point(0,1.5,-5),Point(0,1,0),Vector(0,1,-0.8))
```

Resources: 

[Jamis Buck's "The Ray Tracer Challenge"](http://raytracerchallenge.com/)

[Scratchapixel](https://www.scratchapixel.com/index.html)
