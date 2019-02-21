import numpy as np
n,m,p = input().split()

arr1 = np.array([input().split() for _ in range(int(n))],int)
arr2 = np.array([input().split() for _ in range(int(m))],int)

print(np.concatenate((arr1,arr2),axis=0))