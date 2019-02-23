import numpy as np
n,m = input().split()
arr = np.array([input().split() for _ in range(int(n))], int)
print(np.prod(np.sum(arr,axis=0)))