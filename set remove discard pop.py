n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    code = input().split()
    if code[0] == "pop":
        eval("s."+code[0]+"()")
    else:
        eval("s."+code[0]+"("+code[1]+")")

print(sum(s))