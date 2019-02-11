from itertools import groupby

string = input()

print(*[(len(list(count)),int(group)) for group, count in groupby(string)])