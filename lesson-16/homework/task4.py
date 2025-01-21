import numpy as np

# Define the coefficient matrix and constant vector for the currents
A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

b = np.array([12, -5, 15])

# Solve the system of linear equations
currents = np.linalg.solve(A, b)

I1, I2, I3 = currents
print(f"Currents: I1 = {I1}, I2 = {I2}, I3 = {I3}")