# Python-Raytracer
This project is a raytracer implemented using only Python default libraries.


An example main method is included to render the following scene. 

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9417a08d-c806-46d9-b7d4-6382a476aed3)

The camera is maneuverable to view the scene from different perspectives and angles.

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9f284e0f-280f-4157-8798-f22d552aec25)

To change the viewing angle, reference the following lines in main.py. This creates a camera object and sets the resolution of the image to 566 by 350 pixels with a field of view of pi/2.5. The second line sets the camera's transformation matrix to a view transformation matrix representing a vector pointing from a point (0,1.5,-5) to (0,1,0) with "up" being the vector <0,1,-0.8> relative to the forward direction.
```
  camera = Camera(566,350,math.pi/2.5)
  camera.transform = Matrix.view_transformation(Point(0,1.5,-5),Point(0,1,0),Vector(0,1,-0.8))
```


