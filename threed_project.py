

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
        
def threedplot(x,y,z):

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    
    try:
    
        ax.scatter(x,y,z)
        plt.show()
    except:
        print("Invalid input")
       

      