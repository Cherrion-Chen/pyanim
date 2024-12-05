'''
几何动画框架
开发时间：2024/11/8

通过geo_drive.dll（图形驱动器）高性能的生成确定参数下的图形点坐标，
并在anim对象中明确由动画进程确定图形参数的函数。
对于复杂的几何对象，皆可以通过继承Anim类来实现。
'''

from ctypes import *

#Anim类包含一个初始化函数和一个绘图函数。
class Anim:
    #初始化至少需生成一个ax（轴）对象，便于绘图。
    def __init__(self):
        self.ax = None
    #明确动画进程（第n帧）与图形的关系，在self.ax上绘画并返回之。
    def draw(self, n):
        pass

if __name__ == '__main__':
    path = './geo_drive.dll'
else:
    import os
    path = os.path.join(os.getcwd(), 'pyanim/geo_drive.dll')
dll = cdll.LoadLibrary(path) #导入图形驱动提高性能。

dll.circle.argtypes = (c_double, c_double, c_double)  
dll.ellipse.argtypes = (c_double, c_double)
dll.parabola.argtypes = (c_double, c_double, c_double)
dll.hyperbola.argtypes = (c_double, c_double, c_double, c_double)
dll.free_mem.argtypes = [POINTER(c_double)]

dll.circle.restype = POINTER(c_double)
dll.ellipse.restype = POINTER(c_double)
dll.parabola.restype = POINTER(c_double)
dll.hyperbola.restype = POINTER(c_double)
dll.free_mem.restype = None

'''op = [dll.circle(5,5,2)[i] for i in range(2*629)]
xx, yy = op[:629], op[629:]
plt.axis('equal')
plt.plot(xx,yy)
plt.show()'''

def cir(r, x, y):
    op = dll.circle(r, x, y)
    xx, yy = op[:256], op[256:512]
    dll.free_mem(op)
    return xx,yy # x-cordinates and y-cordinates of the dots on the circle

def ell(a, b):
    op = dll.ellipse(a, b)
    xx, yy = op[:256], op[256:512]
    dll.free_mem(op)
    return xx,yy # x-cordinates and y-cordinates of the dots on the ellipse

def para(c, mn, mx):
    op = dll.parabola(c, mn, mx)
    xx, yy = op[:256], op[256:512]
    dll.free_mem(op)
    return xx,yy # x-cordinates and y-cordinates of the dots on the parabola

def hyper(a, b, mn, mx):
    op = dll.hyperbola(a, b, mn, mx)
    xx, yy = op[:256], op[256:512]
    dll.free_mem(op)
    return xx,yy # x-cordinates and y-cordinates of the dots on the hyperbola

class circle(Anim):
    def __init__(self, fr, fx, fy):
        super(circle, self).__init__()
        self.fx = fx
        self.fy = fy
        self.fr = fr
    def draw(self, n):
        r = self.fr(n) if callable(self.fr) else self.fr
        x = self.fx(n) if callable(self.fx) else self.fx
        y = self.fy(n) if callable(self.fy) else self.fy
        ll = cir(r, x, y)
        return self.ax.plot(ll[0], ll[1])
    
class ellipse(Anim):
    def __init__(self, fa, fb):
        super(ellipse, self).__init__()
        self.fa = fa
        self.fb = fb
    def draw(self, n):
        a = self.fa(n) if callable(self.fa) else self.fa
        b = self.fb(n) if callable(self.fb) else self.fb
        ll = ell(a, b)
        return self.ax.plot(ll[0], ll[1])
    
class parabola(Anim):
    def __init__(self, fc, mn, mx, axis='y'):
        super(parabola, self).__init__()
        self.fc = fc
        self.thre = mn, mx
        self.axis = axis=='y'
    def draw(self, n):
        c = self.fc(n) if callable(self.fc) else self.fc
        ll = para(c, self.thre[0], self.thre[1])
        return self.ax.plot(ll[0], ll[1]) if self.axis else self.ax.plot(ll[1], ll[0])
    
class hyperbola(Anim):
    def __init__(self, fa, fb, mn, mx, axis='y', branch='pos'):
        super(hyperbola, self).__init__()
        self.fa = fa
        self.fb = fb
        self.thre = mn, mx
        self.axis = axis=='y'
        self.branch = branch=='neg'
    def neg(self, x):
        return -x
    def draw(self, n):
        a = self.fa(n) if callable(self.fa) else self.fa
        b = self.fb(n) if callable(self.fb) else self.fb
        xx, yy = hyper(a, b, self.thre[0], self.thre[1])
        if self.branch:
            yy = list(map(self.neg, yy))
        return self.ax.plot(xx, yy) if self.axis else self.ax.plot(yy, xx)

class line(Anim):
    def __init__(self, dot1, dot2):
        super(line, self).__init__()
        self.dot1 = dot1
        self.dot2 = dot2
    def draw(self, n):
        x1, y1 = self.dot1(n) if callable(self.dot1) else self.dot1
        x2, y2 = self.dot2(n) if callable(self.dot2) else self.dot2
        return self.ax.plot([x1,x2],[y1,y2])
