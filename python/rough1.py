import numpy as np

print(np.add(np.array([1]), np.array([])))  # outputs empty array

# print(np.add(np.array([1, 2]), np.array([])))  # raises ValueError

print(np.source(np.add))