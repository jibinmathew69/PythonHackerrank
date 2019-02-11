from itertools import permutations

string,n = input().split()

print(*["".join(tuple) for tuple in permutations(sorted(string),int(n))],sep="\n")