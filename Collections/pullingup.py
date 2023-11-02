import collections
t = int(input())

for i in range(t):
    n, b = int(input()), collections.deque(map(int, input().split()))

    if n == 0:
        print("No")

    else:
        for i in range(len(b)):
            if b[-1] > b[0]:
                block = b.pop()
            else:
                block = b.popleft()

            if len(b) == 0:
                print("Yes")
                continue
            if b [-1] > block or b[0] > block:
                print("No")
                break
