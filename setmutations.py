n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    opr, size = input().split()
    set2 = set(input().split())

    if opr == 'intersection_update':
        A.intersection_update(set2)

    elif opr == 'update':
        A.update(set2)

    elif opr == 'symmetric_difference_update':
        A.symmetric_difference_update(set2)

    elif opr == 'difference_update':
        A.difference_update(set2)


sum = 0
for i in A:
    sum += int(i)
print(sum)
