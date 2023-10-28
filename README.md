# Python-Raytracer
This project is a raytracer implemented using only Python default libraries.


An example main method is included to render the following scene. 

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9417a08d-c806-46d9-b7d4-6382a476aed3)

The camera is maneuverable to view the scene from different perspectives and angles.

![image](https://github.com/grahamasam/Python-Raytracer/assets/107145436/9f284e0f-280f-4157-8798-f22d552aec25)

'''
  camera = Camera(566,350,math.pi/2.5)
  camera.transform = Matrix.view_transformation(Point(0,1.5,-5),Point(0,1,0),Vector(0,1,-0.8))
  '''
