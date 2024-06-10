import numpy as np
import matplotlib.pyplot as plt

def make_hexagons(centres):
    hexagons = []
    n = 6
    thetas = np.linspace(0, 2 * np.pi, n)

    for c in centres:
        for d in centres:
            x = c + np.cos(thetas)
            y = d + np.sin(thetas)
            hexagons.append([np.array(np.append(x, x[0])), np.array(np.append(y, y[0]))])
    
    return hexagons

if __name__ == "__main__":
    num_hexagons = 20
    radius = np.pi/4
    centres = np.arange(-1 * np.pi, radius + num_hexagons * 3 * radius, 3 * radius)

    hexagons = make_hexagons(centres)

    plt.figure(figsize=(10, 10))
    for hexagon in hexagons:
        x_coords = hexagon[0]
        y_coords = hexagon[1]
        plt.plot(1.5 * x_coords + np.sin(y_coords), 1.5 * y_coords + np.sin(x_coords), c = "black")

    plt.axis('off')
    
    filename = __file__.split("/")[-1][:-3]
    plt.savefig(f"../patterns/{filename}.png")