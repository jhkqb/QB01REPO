import numpy as np
import matplotlib.pyplot as plt

# Parameters of the ellipse
a = 5  # Semi-major axis
b = 3  # Semi-minor axis
h = 0  # x-coordinate of the center
k = 0  # y-coordinate of the center

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 1000)  # Angle from 0 to 2π
x = h + a * np.cos(theta)  # Parametric equation for x
y = k + b * np.sin(theta)  # Parametric equation for y

# Plot the ellipse
plt.figure(figsize=(6, 6))
plt.plot(x, y, label=f"Ellipse: x^2/{a}^2 + y^2/{b}^2 = 1")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")  # y-axis
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
plt.title("Graph of an Ellipse")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

