from itertools import product


x = int(input())+1
y = int(input())+1
z = int(input())+1
n = int(input())


filtered = list(filter(lambda tuple: sum(tuple)!=n,  product(range(x), range(y), range(z))))

print([list(x) for x in filtered])