from itertools import combinations

string,n = input().split()

for i in range(1,int(n)+1):
    print(*["".join(tuple) for tuple in combinations(sorted(string),i)],sep="\n")