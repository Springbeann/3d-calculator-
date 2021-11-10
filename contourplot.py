import numpy as np

import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


def contour(x, y, z, a, b, c):
    fig = plt.figure(figsize=(4,4))
    x_vector = np.linspace(x, y, z)
    y_vector = np.linspace(a, b, c)

    X_mesh, Y_mesh = np.meshgrid(x_vector, y_vector)
    Z = f(X_mesh, Y_mesh)

    ax = plt.axes(projection='3d')
    ax.contour3D(X_mesh, Y_mesh, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.plot_wireframe(X_mesh, Y_mesh, Z, color='pink')
    ax.set_title('wireframe');
    plt.show()