import re

for _ in range(int(input())):
    string = input()
    print('Valid' if all([re.search(r'^[A-Za-z0-9]{10}$', string), re.search(r'([A-Z].*){2}', string), re.search(r'([0-9].*){3}', string), not re.search(r'.*(.).*\1', string)]) else "Invalid")
