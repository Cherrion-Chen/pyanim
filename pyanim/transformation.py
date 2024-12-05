from .basic import *
import numpy as np

class move(Anim):
    def __init__(self, original, delta_x, delta_y):
        super(move, self).__init__()
        self.ori = original
        self.x = delta_x
        self.y = delta_y
    def draw(self, n):
        xx, yy = self.ori.draw(n)[0].get_data()
        arr = np.array([xx, yy])
        dx = self.x(n) if callable(self.x) else self.x
        dy = self.y(n) if callable(self.y) else self.y
        arr = arr + np.array([[dx], [dy]])
        return self.ax.plot(arr[0], arr[1])

class linear(Anim):
    def __init__(self, original, mat):
        super(linear, self).__init__()
        self.ori = original
        self.mat = mat
    def draw(self, n):
        xx, yy = self.ori.draw(n)[0].get_data()
        arr = np.array([xx, yy])
        mat = self.mat if callable(self.mat) else self.mat
        arr = mat @ arr
        return self.ax.plot(arr[0], arr[1])
    
def reflect(original, axis):
    if axis=='x':
        mat = np.array([[1, 0], [0, -1]])
    else:
        mat = np.array([[-1, 0], [0, 1]])
    return linear(original, mat)

def rotate(original, ang):
    if callable(ang):
        def mat(n):
            return np.array([[np.cos(ang(n)), -np.sin(ang(n))], [np.sin(ang(n)), np.cos(ang(n))]])
    else:
        mat = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    return linear(original, mat)
