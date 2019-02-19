import re
for _ in range(int(input())):
    print("YES" if str(bool(re.match(r'[789][0-9]{9}$', input()))) else "NO")