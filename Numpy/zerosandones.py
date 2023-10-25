import numpy

n = list(map(int, input().split()))
user_input = numpy.array(n)

print(numpy.zeros(user_input, dtype = int))
print(numpy.ones(user_input, dtype = int))
