import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_waves_x = 20  # Number of sine waves in x-direction
num_waves_y = 20  # Number of sine waves in y-direction
max_amplitude = 1.0
min_amplitude = 0.1
max_frequency = 2.0
min_frequency = 0.5
wave_length = 4 * np.pi  # Length of the sine wave
x = np.linspace(0, wave_length, 500)

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

for j in range(num_waves_y):
    for i in range(num_waves_x):
        # Calculate amplitude and frequency for each wave
        amplitude = max_amplitude - (j * (max_amplitude - min_amplitude) / (num_waves_y - 1))
        frequency = max_frequency - (i * (max_frequency - min_frequency) / (num_waves_x - 1))
        
        # Generate the sine wave
        y = amplitude * np.sin(frequency * x)
        
        # Offset each wave horizontally and vertically
        ax.plot(x + i * wave_length / num_waves_x, y - j * (max_amplitude + 0.5), color='black', linewidth=0.5)

# Adjust plot
ax.set_aspect('equal')
ax.axis('off')
plt.show()
