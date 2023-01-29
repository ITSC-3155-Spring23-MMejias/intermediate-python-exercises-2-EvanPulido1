# Evan Pulido
# ITSC 3155

# Links that helped me write the code and use numpy:
# https://www.w3schools.com/python/numpy/numpy_random.asp
# https://numpy.org/doc/stable/reference/generated/numpy.median.html
# https://numpy.org/doc/stable/reference/generated/numpy.std.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html

# Imports numpy
import numpy as np

# Calls the random module from numpy
from numpy import random

# 10 random float numbers that each range from 0 to 1
x1 = random.rand()
x2 = random.rand()
x3 = random.rand()
x4 = random.rand()
x5 = random.rand()
x6 = random.rand()
x7 = random.rand()
x8 = random.rand()
x9 = random.rand()
x10 = random.rand()

# An array of all the random float numbers
number_list = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])

# Print out the array to see the numbers
print(number_list)
# Print the mean of the 10 numbers. numpy has a mean method that does all the equations for us
print('Mean: ' + str(np.mean(number_list)))
# Print the median of the 10 numbers
print('Median: ' + str(np.median(number_list)))
# Print the standard deviation of the 10 numbers
print('Standard Deviation: ' + str(np.std(number_list)))