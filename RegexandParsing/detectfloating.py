import re

s = int(input())
ex = "[+-.]{0,1}[0-9]{0,}[.][0-9]{1,}"
for i in range(s):
    print(bool(re.fullmatch(ex, input())))
