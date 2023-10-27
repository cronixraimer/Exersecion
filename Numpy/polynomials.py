from numpy import polyval

P = list(map(float, input().split()))
x = int(input())

print(polyval(P, x))
