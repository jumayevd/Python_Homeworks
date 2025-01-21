from math import exp
import numpy as np

def calculate_power(base, exponent):
    return base**exponent

bases = np.array([2,3,4,5])
exponents = np.array([1,2,3,4])

vectorized_power = np.vectorize(calculate_power)
powered_values = vectorized_power(bases, exponents)

print("Powered values: ", powered_values)

