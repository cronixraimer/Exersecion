import re

s = int(input())

pattern = r'^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*\d){3,})[a-zA-Z0-9]{10}$'

for i in range(s):
    phone = input()

    if re.match(pattern, phone):
        print('Valid')
    else:
        print('Invalid')
