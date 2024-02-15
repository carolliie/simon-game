import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    point.set_data([], [])
    return point,

def animate(i):
    x = i
    y = 0
    point.set_data(x, y)
    return point,

fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(-1, 1)

point, = ax.plot([], [], marker='o', color='r')

ani = animation.FuncAnimation(fig, animate, frames=300, init_func=init, blit=True, interval=20)

plt.show()
