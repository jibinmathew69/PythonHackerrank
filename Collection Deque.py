from collections import deque
n = int(input())
s = deque()

for _ in range(n):
    code = input().split()
    if "pop" in code[0]:
        eval("s."+code[0]+"()")
    else:
        eval("s."+code[0]+"("+code[1]+")")

print(*s)