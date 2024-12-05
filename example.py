from pyanim import *
from math import cos, sin

def a(n):
    return 2*cos(n/18)

def b(n):
    return 2*sin(n/18)

def a1(n):
    return cos(n/18)

def b1(n):
    return sin(n/18)

def c(n):
    return 0.2*sin(n/18)+0.3

def x(n):
    return 2*cos(n/18)

o = circle(0.5,x,0)
h = hyperbola(c,1,-2,2,'x')
g = [ellipse(a,b), o,transformation.move(o,a1,b1),h,transformation.reflect(h,'y')]
show_anim(g,n=200, lim=((-4,4),(-4,4)))
