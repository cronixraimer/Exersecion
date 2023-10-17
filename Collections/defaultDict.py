from collections import defaultdict

n, m = map(int, input().split())

group_a = defaultdict(list)
group_b = defaultdict(list)

# Read words of group A
for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

# Read words of group B and print positions
for i in range(1, m + 1):
    word = input()
    positions = group_a[word]
    if positions:
        print(" ".join(map(str, positions)))
    else:
        print(-1)
