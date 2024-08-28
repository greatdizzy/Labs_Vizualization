from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def vector_field(x, y, z):
    u = (x + z) / x**2
    v = (y + x) / y**2
    w = (z + x) / z**2
    return u, v, w

def euler_integration(x0, y0, z0, field_func, t0, t1, dt):
    t = np.arange(t0, t1, dt)
    path = np.zeros((len(t), 3))
    path[0, :] = [x0, y0, z0]

    for i in range(1, len(t)):
        u, v, w = field_func(path[i-1, 0], path[i-1, 1], path[i-1, 2])
        path[i, 0] = path[i-1, 0] + u * dt
        path[i, 1] = path[i-1, 1] + v * dt
        path[i, 2] = path[i-1, 2] + w * dt

    return path

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Інтеграція та візуалізація ліній потоку
colors = ['blue', 'green', 'red', 'purple', 'orange']
start_points = [(-10, -10, -10), (0, 0, 0), (10, 10, 10), (-10, 10, -10), (10, -10, 10)]
for (x0, y0, z0), color in zip(start_points, colors):
    path = euler_integration(x0, y0, z0, vector_field, 0, 10, 0.1)
    ax.plot(path[:, 0], path[:, 1], path[:, 2], label=f'Start: ({x0}, {y0}, {z0})', color=color, alpha=0.7)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Streamlines of Vector Field')
ax.legend()
plt.show()
