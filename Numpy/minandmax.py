import numpy

n , m = map(int, input().split())

user_input = []

for i in range(n):
    user_input.append(input().split())

x = numpy.array(user_input, int)

max_input = numpy.min(x, axis = 1)

print(numpy.max(max_input))
