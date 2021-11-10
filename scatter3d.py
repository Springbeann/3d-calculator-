
import numpy as np
 
import matplotlib.pyplot as plt 
def scatter(x,y,z):
    scatterplot = plt.figure(figsize=(4,4))
    ax = plt.axes(projection='3d')
    zline = np.linspace(x,y,z)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap= 'Greens');
    plt.show()
