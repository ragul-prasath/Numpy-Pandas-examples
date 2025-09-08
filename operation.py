'''
1. Create a 3x3 matrix with values from 1 to 9.
2. Generate an array of 10 random integers between 1 and 100.
3. Create a 5x5 identity matrix using NumPy
'''
import numpy as np
from numpy import random
print(random.randint(1,9, size=(3, 5)))
print(random.randint(1,100,size=(10)))
print(np.eye(5, 5, dtype=int))