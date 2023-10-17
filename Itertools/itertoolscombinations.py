from itertools import combinations

s, k = input().split()
s = s.upper()

for i in range(1, int(k) + 1):
    t = sorted(list(combinations(sorted(s), i)))
    for j in t:
        print(''.join(j))
