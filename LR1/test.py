import numpy as np
import matplotlib.pyplot as plt

# Define the functions for the lines
x1_values = np.linspace(0, 10, 200)
line1 = (12 - 6 * x1_values)
line2 = (11 - 3 * x1_values)
line3 = (11 - 2 * x1_values)

# Set up the plot
plt.figure(figsize=(10, 8))

# Plot each line
plt.plot(x1_values, line1, label="6x1 + x2 = 12")
plt.plot(x1_values, line2, label="3x1 + x2 = 11")
plt.plot(x1_values, line3, label="2x1 + x2 = 11")

# Shading the feasible region
plt.fill_between(x1_values, np.maximum(line2, line3), line1, where=(line1 >= line2) & (line1 >= line3) & (line2 <= line3), color='gray', alpha=0.3)

# Mark intersection points
# Line1 and Line2 intersection
A_x1, A_x2 = np.linalg.solve([[6, 1], [3, 1]], [12, 11])
# Line1 and Line3 intersection
B_x1, B_x2 = np.linalg.solve([[6, 1], [2, 1]], [12, 11])
# Line2 and Line3 intersection
C_x1, C_x2 = np.linalg.solve([[3, 1], [2, 1]], [11, 11])

# Plot intersection points
plt.plot(A_x1, A_x2, 'ro', label="Intersection A")
plt.plot(B_x1, B_x2, 'go', label="Intersection B")
plt.plot(C_x1, C_x2, 'bo', label="Intersection C")

# Gradient and anti-gradient direction (for visualizing gradient direction)
grad = np.array([1, 1])  # Gradient vector
x_grad, y_grad = [5], [5]  # Starting point for the gradient
plt.quiver(x_grad, y_grad, grad[0], grad[1], angles='xy', scale_units='xy', scale=1, color='purple', label="Gradient (1,1)")

# Plot constant level lines perpendicular to gradient
for c in range(10, 16, 2):
    plt.plot(x1_values, c - grad[0] * x1_values, linestyle='--', color='blue')

# Labeling
plt.xlim(0, 10)
plt.ylim(0, 15)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Lines, Feasible Region, Gradient and Level Lines")
plt.legend()
plt.grid(True)
plt.show()
