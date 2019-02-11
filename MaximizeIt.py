K,M = map(int,input().split())
values = []
values = (list(map(int,input().split()))[1:] for i in range(K))

from itertools import product

sums = map(lambda x: sum(i**2 for i in x)%M, product(*values))

print(max(sums))