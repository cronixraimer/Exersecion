import numpy as n

l = list(map(int, input().split()))
a, b = [n.array([input().split() for i in range(l[0])], int) for i in range(2)]


print(n.add(a, b))
print(n.subtract(a, b))
print(n.multiply(a, b))
print(n.floor_divide(a, b))
print(n.mod(a, b))
print(n.power(a, b))
