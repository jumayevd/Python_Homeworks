import numpy as np

# Define the power function
def calculate_power(base, exponent):
    return base**exponent

# Numbers and powers arrays
bases = np.array([2,3,4,5])
exponents = np.array([1,2,3,4])

# Vectorize the function
vectorized_power = np.vectorize(calculate_power)

# Apply the vectorized function
powered_values = vectorized_power(bases, exponents)

print("Powered values: ", powered_values)

