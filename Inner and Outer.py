import numpy as np
a = np.array([input().split()],int)
b = np.array([input().split()],int)

print(np.inner(a,b)[0][0])
print(np.outer(a,b))