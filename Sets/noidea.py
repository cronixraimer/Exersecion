n, m = map(int, input().split())
arr = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

count = 0

for i in arr:
    if i in a:
        count += 1
    elif i in b:
        count -= 1

print(count)
