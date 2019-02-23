import numpy as np
np.set_printoptions(legacy='1.13')
a = np.array([input().split() for _ in range(int(input()))],float)
print(np.linalg.det(a))