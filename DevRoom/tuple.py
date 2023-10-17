import hashlib
n = int(input())
integer = map(int, input().split())
t = tuple(integer)
print(hash(t))
