import numpy
numpy.set_printoptions(legacy = '1.13')

n = list(map(float, input().split()))
user_input = numpy.array(n)

print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
