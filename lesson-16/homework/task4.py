import numpy as np

A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

b = np.array([12, -5, 15])

x = np.linalg.solve(A, b)

print("Solution for I1, I2, I3 :", x)