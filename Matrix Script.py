import re
import operator
from functools import reduce

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

string = "".join(reduce(operator.concat, [list(i) for i in zip(*matrix)]))
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", string))
