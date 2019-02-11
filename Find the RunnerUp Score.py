count = input()
scores = set(map(int,input().split(" ")))
print(sorted(scores,reverse=True)[1])