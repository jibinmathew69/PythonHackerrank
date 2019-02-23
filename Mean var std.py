import numpy as np
n,m = input().split()
arr = np.array([input().split() for _ in range(int(n))], int)
np.set_printoptions(legacy='1.13')
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr))