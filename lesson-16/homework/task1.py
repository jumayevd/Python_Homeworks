import numpy as np

# Define the conversion function
def fahrenheit_to_celcius(f):
    return ((f-32)*5/9)

# Fahrenheit array
temperatures_f = np.array([32,68,100,212,77])

# Vectorize the function
vectorized_conversion = np.vectorize(fahrenheit_to_celcius)

# Apply the vectorized function
temperatures_c = vectorized_conversion(temperatures_f)

print("Temperatures in Celcius: ", temperatures_c)
