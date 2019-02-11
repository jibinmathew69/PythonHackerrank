from itertools import combinations

n = input()
chars = input().split(" ")

k = int(input())

combi = list(combinations(chars,k))

print(len(list(filter(lambda c: 'a' in c, combi)))/len(combi))