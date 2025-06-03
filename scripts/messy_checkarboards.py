import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import matplotlib.patches as patches
import numpy as np
import random
import colorsys

def saturate_color(color, saturation_factor=1.5):
    r, g, b = mcolors.to_rgb(color)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    s = min(1, s * saturation_factor)  # Cap at 1
    r_new, g_new, b_new = colorsys.hsv_to_rgb(h, s, v)
    return (r_new, g_new, b_new)

def generate_variable_grid(rows=20, cols=20, 
                           min_width=0.2, max_width=1, 
                           min_height=0.2, max_height=1, 
                           colors=None, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    if colors is None:
        colors = ["#374596","#d9c8cf","#b1aaad","#0099d6","#eeb64c","#e8705e","#9e404a","#49383d","#a7bad8","#e04155"]

    widths = np.random.uniform(min_width, max_width, cols)
    heights = np.random.uniform(min_height, max_height, rows)

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_aspect('equal')

    colcolours = [random.sample(colors, 3) for _ in range(cols)]
    colors = np.zeros((rows, cols), dtype=object)

    y = 0
    for i in range(rows):
        x = 0
        height = heights[i]
        for j in range(cols):
            width = widths[j]
            color = random.choice(list(set(colcolours[j]) - set([colors[i-1, j]]) - set([colors[i, j-1]])))
            rect = plt.Rectangle((x, y), width, height,
                                 facecolor=saturate_color(color, saturation_factor=1.2),
                                 
                                 linewidth=0.5)
            ax.add_patch(rect)
            colors[i, j] = color
            x += width
        y += height

    ax.set_xlim(0, sum(widths))
    ax.set_ylim(0, sum(heights))
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("../patterns/messy_checkarboards.png", dpi=300, bbox_inches='tight')

generate_variable_grid()