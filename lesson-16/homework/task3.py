import numpy as np

# Define the coefficient matrix and constant vector
A = np.array([[4, 5, 6], 
             [3, -1, 1], 
             [2, 1, -2]])

b  = np.array([7, 4, 5])

# Solve the system of linear equations
solutions = np.linalg.solve(A, b)

x, y, z = solutions
print(f"Solutions: x = {x}, y = {y}, z = {z}")