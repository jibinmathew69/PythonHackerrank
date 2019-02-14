nm = input()
parent = list(input().split())
happy = set(input().split())
sad = set(input().split())

print(sum([(item in happy)-(item in sad) for item in parent]))