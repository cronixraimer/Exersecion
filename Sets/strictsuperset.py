n = set(map(int, input().split()))

m = int(input())
strict_s = []

for i in range(m):
    a = set(map(int, input().split()))

    check_subset = a.difference(n)
    strict_s += check_subset

if len(strict_s) == 0:
    print("True")
else:
    print("False")
