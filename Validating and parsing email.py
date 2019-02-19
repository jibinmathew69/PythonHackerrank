import email.utils
import re

for _ in range(int(input())):
    x, y = input().split(' ')
    if re.match(r'<[a-z]{1}[a-z0-9._-]+@[a-z]+\.[a-z]{1,3}>',y,re.I):
        print(email.utils.formataddr(y))