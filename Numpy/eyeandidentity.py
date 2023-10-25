import numpy
numpy.set_printoptions(legacy = '1.13')

print(numpy.eye(*list(map(int, input().split())))) #before list * this  unpack the list into separate arguments as numpy.eye  expects separate integer arguments
