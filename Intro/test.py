x = int(input())
i = 1
while i <= x:
    a = list(map(int, input().split()))
    c = a[0] + a[1]
    print(c)
    i += 1
