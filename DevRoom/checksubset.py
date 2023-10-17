
n = int(input())

for i in range(n):
    a_1 = int(input())
    a = set(map(int, input().split()))

    b_1 = int(input())
    b = set(map(int, input().split()))

    check_subset = a.difference(b)

    if len(check_subset) == 0:
        print("True")
    else:
        print("False")
