import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

def thomas(xyz, *, b):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = np.sin(y) - b * x
    y_dot = np.sin(z) - b * y
    z_dot = np.sin(x) - b * z
    return np.array([x_dot, y_dot, z_dot])


def plot_thomas(xyz, *, b):

    dt = 0.01
    num_steps = 100000

    xyzs = np.empty((num_steps + 1, 3))

    xyzs[0] = (0.2, 0.1, 0.1)
    # xyzs[0] = [np.random.randn(1)[0], np.random.randn(1)[0], np.random.randn(1)[0]]

    for i in range(num_steps):
        xyzs[i + 1] = xyzs[i] + thomas(xyzs[i]) * dt

    # Plot
    ax = plt.figure(figsize=(8, 8)).add_subplot(projection='3d')

    ax.plot(*xyzs.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Thomas Attractor")

    plt.tight_layout()
    plt.show()

    return
