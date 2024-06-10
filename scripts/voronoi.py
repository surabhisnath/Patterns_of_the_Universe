import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
np.random.seed(27)

# Good ref: https://github.com/jmespadero/pyDelaunay2D

def sunflower_points(num_pts, plane_size, alpha=0.6):
    # Golden angle in radians
    golden_angle = np.pi * (3 - np.sqrt(5))
    
    # Initialize arrays for x and y coordinates
    x = np.zeros(num_pts)
    y = np.zeros(num_pts)
    
    # Generate points
    for i in range(num_pts):
        # Distance from center varies according to a power law
        r = i ** alpha
        theta = i * golden_angle
        
        x[i] = r * np.cos(theta) + plane_size/2
        y[i] = r * np.sin(theta) + plane_size/2
    
    return x, y

if __name__ == "__main__":
    # Set a plane size
    plane_size = 100

    # Randomly sample `num_pts` starting points
    num_pts = 800

    # Set type to random or sunflower
    type = "random"

    # Get coordinates of `num_pts` points
    if type == "random": 
        x_coords, y_coords = np.random.randint(0, plane_size, num_pts), np.random.randint(0, plane_size, num_pts)

    if type == "sunflower":
        x_coords, y_coords = sunflower_points(num_pts, plane_size)

    # For each coordinate, find triangles, and find circumcentres and vornoi connecting adjacent circumcentres
    tri = Delaunay(list(zip(x_coords, y_coords)))
    vor = Voronoi(list(zip(x_coords, y_coords)))

    fig, ax = plt.subplots(figsize=(plane_size//8, plane_size//8))
    # comment next 2 lines to just visualise the final voronoi plot
    # plt.scatter(x_coords, y_coords)
    # plt.triplot(x_coords, y_coords, tri.simplices)
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, show_points=False)

    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, plane_size)
    plt.ylim(0, plane_size)

    filename = __file__.split("/")[-1][:-3]
    plt.savefig(f"../patterns/{filename}.png")