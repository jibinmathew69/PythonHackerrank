import re
match = re.search(r'([^\W_])\1+',input())
print(match.group(1) if match else -1)