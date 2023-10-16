import re
x = int(input())

if 0 < x < 100:

    for i in range(x):
        try:
            re.compile(input())
            print(True)
        except re.error:
            print(False)
