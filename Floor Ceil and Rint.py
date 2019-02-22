import numpy as np
a = np.array(input().split(),dtype=float)

print(np.floor(a),np.ceil(a),np.rint(a),sep='\n')