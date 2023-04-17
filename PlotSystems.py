import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

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
        xyzs[i + 1] = xyzs[i] + thomas(xyzs[i], b=b) * dt

    # Create a scatter trace with x, y, and z data
    trace = go.Scatter3d(x=xyzs[:, 0], y=xyzs[:, 1], z=xyzs[:, 2], mode='lines')

    # Create a layout object with axes labels and a title
    layout = go.Layout(scene=dict(xaxis_title='X Axis', yaxis_title='Y Axis', zaxis_title='Z Axis'),
                       title='Thomas Attractor')

    # Create a figure object with the trace and layout
    fig = go.Figure(data=[trace], layout=layout)

    return fig
