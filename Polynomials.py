import numpy as np

coef = list(map(float,input().split()))

print(np.polyval(coef, int(input())))