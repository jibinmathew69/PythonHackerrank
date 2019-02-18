n,x = map(int,input().split())
z = []
for i in range(x):
    z.append(list(map(float,input().split())))

for marks in zip(*z):
    print(sum(marks)/x)