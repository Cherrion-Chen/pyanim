import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from .basic  import *
from . import transformation

#根据参数范围和总帧数给出一个参数变化函数。
def ran(start, end, num=100):
    def f(n):
        return start + 1/(1+math.pow(2, -10*n/num))*(end-start)
    return f

#核心功能：绘制动画（可以保存）。
def show_anim(objs, n=128, freq=24, lim=False, show=True, save=False):
    fig, ax= plt.subplots()
    for i in objs:
        i.ax = ax
    def animate(n):
        ax.clear()
        ax.axis('equal')
        if lim:
            ax.set_xlim(lim[0])
            ax.set_ylim(lim[1])
        return [i.draw(n) for i in objs]
    an = FuncAnimation(fig, animate, frames=range(n), interval=1000/freq)
    if save:
        an.save(save, writer='ffmpeg')
    if show:
        plt.show()
