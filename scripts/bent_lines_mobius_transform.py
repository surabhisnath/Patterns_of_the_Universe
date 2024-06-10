import numpy as np
import matplotlib.pyplot as plt

# ref: https://www.johndcook.com/blog/2020/09/23/circles-to-circles/

def plot_lines(lines):
    plt.figure(figsize=(10,10))
    for z in lines:
        plt.plot(z['real'], z['imag'], c="black")
    plt.xlim(-0.05, 0.05)   # need to change is change num_lines
    plt.ylim(-0.05, 0.05)
    plt.axis('off')
    return plt

def mobius(z):
    den = (z["real"]**2 + z["imag"]**2)
    return {"real": z["real"]/den,
            "imag": -1 * z["imag"]/den}

if __name__ == "__main__":
    
    num_pts = 600
    line = np.linspace(-100, 100, num_pts)

    num_lines = 50

    lines = []
    dist = 10

    for nl in range(1, num_lines + 1):
        lines.extend([
                {"real": np.array([dist * nl]*num_pts), "imag": line},
                {"real": np.array([-dist * nl]*num_pts), "imag": line},
                {"real": line, "imag": np.array([dist * nl]*num_pts)},
                {"real": line, "imag": np.array([-dist * nl]*num_pts)} 
            ])

    plt = plot_lines([mobius(z) for z in lines])

    filename = __file__.split("/")[-1][:-3]
    plt.savefig(f"../patterns/{filename}.png")