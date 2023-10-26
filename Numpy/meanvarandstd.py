import numpy

n , m = map(int, input().split())

user_input = []

for i in range(n):
    user_input.append(input().split())

x = numpy.array(user_input, int)

print(numpy.mean(x, axis = 1))
print(numpy.var(x, axis = 0))
print(round(numpy.std(x, axis = None), 11))
