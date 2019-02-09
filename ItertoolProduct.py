a = []
a.append( map(int,input().split()))
a.append(map(int,input().split()))

from itertools import product
print(*list(product(*a)))