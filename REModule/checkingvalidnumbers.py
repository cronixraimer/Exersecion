import re

s = int(input())

ex = r'[789][0-9]{9}'

for i in range(s):
    phone = input()

    if re.match(ex, phone) and len(phone) == 10:
        print('YES')
    else:
        print('NO')
