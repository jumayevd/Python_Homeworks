import numpy as np

A = np.array([[4, 5, 6], 
             [3, -1, 1], 
             [2, 1, -2]])

b  = np.array([7, 4, 5])

x = np.linalg.solve(A, b)

print("Solution is : ", x)