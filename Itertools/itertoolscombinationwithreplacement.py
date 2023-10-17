from itertools import combinations_with_replacement

s, k = input().split()
s = s.upper()

for i in range(int(k), int(k) + 1):
    t = sorted(list(combinations_with_replacement(sorted(s), i)))
    for j in t:
        print(''.join(j))
