n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

union_set = set1.intersection(set2)

count_union = len(union_set)

print(count_union)
