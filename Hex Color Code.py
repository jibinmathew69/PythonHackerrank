import re
for _ in range(int(input())):
    # codes = re.findall(r'(?<=\s|:)#[a-f0-9]{3,6}', input(), flags=re.I) Length between 3 and 6 will be accepted!
    codes = re.findall(r'[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', input(), flags=re.I)

    if codes:
        print(*codes,sep="\n")