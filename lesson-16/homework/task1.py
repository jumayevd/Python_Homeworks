import numpy as np


@np.vectorize
def fahrenheit_to_celcius(f):
    return ((f-32)*5/9)

temperatures_f = np.array([32,68,100,212,77])
vectorized_conversion = np.vectorize(fahrenheit_to_celcius)
temperatures_c = vectorized_conversion(temperatures_f)
temperatures_c =np.round(temperatures_c, 1)

print("Temperatures in Celcius: ", temperatures_c)
