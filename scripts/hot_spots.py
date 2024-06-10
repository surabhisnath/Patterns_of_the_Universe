import numpy as np
import matplotlib.pyplot as plt

def make_circles(centres):
    circles = []
    thetas = np.linspace(0, 2 * np.pi, 200)
    for c in centres:
        for d in centres:
            x = []
            y = []
            for theta in thetas:
                x.append(c + radius * np.cos(theta))
                y.append(d + radius * np.sin(theta))
            circles.append([np.array(x), np.array(y)])
    
    return circles

if __name__ == "__main__":
    num_circles = 20
    radius = np.pi/8
    centres = np.arange(-1 * np.pi, radius + num_circles * 3 * radius, 3 * radius)

    circles = make_circles(centres)

    plt.figure(figsize=(10, 10))
    for circle in circles:
        x_coords = circle[0]
        y_coords = circle[1]
        plt.plot(1.5 * x_coords + np.sin(y_coords), 1.5 * y_coords + np.sin(x_coords), c = "black")

    plt.axis('off')

    filename = __file__.split("/")[-1][:-3]
    plt.savefig(f"../patterns/{filename}.png")