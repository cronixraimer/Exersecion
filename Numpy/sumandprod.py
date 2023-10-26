import numpy

n, m = map(int, input().split())

user_input = []

for i in range(n):
    user_input.append(input().split())

x = numpy.array(user_input, int)

sum = numpy.sum(x, axis = 0)

print(numpy.prod(sum))
