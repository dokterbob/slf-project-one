from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #<-- Note the capitalization
import numpy as np


def plot_data(data):
    # Create figure
    fig = plt.figure()

    ax = Axes3D(fig)

    X = np.arange(0, data.shape[0], 1.0)
    Y = np.arange(0, data.shape[1], 1.0)
    X, Y = np.meshgrid(X, Y)

    # This is the data
    Z = data

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
