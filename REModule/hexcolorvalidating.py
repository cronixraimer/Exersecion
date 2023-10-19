import re

s = int(input())

pattern = re.compile(r'#[0-9A-Fa-f]{6}(?=[;,)])|#[0-9A-Fa-f]{3}(?=[;,)])')

x = pattern.findall("\n".join([input() for i in range(s)]))
for i in x:
    print(i)
