from itertools import combinations_with_replacement

string,n = input().split()

print(*["".join(tuple) for tuple in combinations_with_replacement(sorted(string),int(n))],sep="\n")