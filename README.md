# Pyanim
An animation framework based on Python.

Welcome to Pyanim! This is an animation framework based on Python, intended to provide Maths researchers, learers and teachers with a easy kit to learn about how the geometry objects vary with the change of certain parameters.

The package contains a initiative Python file(init.py), the file that encapsulates the basic geometry objects(basic.py) and a toolkit for transformation(transformaion.py).

In basic.py, a class named "Anim" is provided. It must have a method "draw", which'll be called when generating the animation, clarifying the relationship between frame count and image. A dynamic link lib is written to accelerate the calculation, which provides you with generator of basic geometry objects.

High performance generation of geo_drive.dll (graphics driver) to determine the graphics point coordinates under the parameters, and explicitly in the anim object by the animation process to determine the graphics parameters of the function.

For complex geometry objects, all can be implemented by inheriting the Anim class.

As a highschool student, this is the first time I have ever shared my project on GitHub. Despite the huge space for improvement, I still hope my work will bring you convenience or inspirations! 
