import re
s = input()
x = re.search(r"([a-zA-Z0-9])\1", s)

if x:
    print(m.group(1))
else:
    print(-1)
