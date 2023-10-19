import re

s = int(input())

x = r'[a-zA-Z0-9]+ <[a-z0-9]+[-_.a-zA-Z0-9]+@[a-z]+[.][a-z]{1,3}>'

em = []
for i in range(s):
    email = input()

    if re.match(x,email):
        em.append(email)
for i in em:
    print(i)
