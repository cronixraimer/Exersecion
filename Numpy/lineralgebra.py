import numpy

n = int(input())

user_input = []

for i in range(n):
    user_input.append(input().split())

x = numpy.array(user_input, float)

print(round(numpy.linalg.det(x), 3))
