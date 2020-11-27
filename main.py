from raytracer import Raytracer
from sphere import *
from materials import *
from math_things import V3

out = 'out.bmp'
r = Raytracer(500, 500)


#ahora haremos un snowman
#algo interesante es que hayq ue poner primero los objetos que estan 
#mas adelante y despues los que estan mas atras
#al momento no termino de entender el por qué
r.scene = [

	Sphere(V3(0.2,-5,-8),0.12,snowman_teeth),
	Sphere(V3(-0.2,-5,-8),0.12,snowman_teeth),
	Sphere(V3(0.6,-5.1,-8),0.12,snowman_teeth),
	Sphere(V3(-0.6,-5.1,-8),0.12,snowman_teeth),
	Sphere(V3(0.5,-6.8,-8),0.12,black_botton),
	Sphere(V3(-0.5,-6.8,-8),0.12,black_botton),
	Sphere(V3(0.5,-6.7,-8),0.25,snow),
	Sphere(V3(-0.5,-6.7,-8),0.25,snow),
    Sphere(V3(0.5,-6.7,-8),0.3,black_botton),
	Sphere(V3(-0.5,-6.7,-8),0.3,black_botton),
	Sphere(V3(0,-5.8,-8),0.4,buxbunny),

	Sphere(V3(0,3,-7),0.9,black_botton),
	Sphere(V3(0,0,-7),0.7,black_botton),
	Sphere(V3(0,-2.7,-7),0.5,black_botton),	
	Sphere(V3(0,-5.8,-8),1.4,snow),
	Sphere(V3(0,-2,-8),2.3,snow),
	Sphere(V3(0,3,-8),3.3,snow),
]


r.render()
r.display(out)