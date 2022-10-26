import numpy as np
from itertools import product

freq = np.zeros(11, dtype=np.int16)
for i, j in product(range(1, 7), range(1, 7)):
    freq[i + j - 2] += 1

print(freq)
