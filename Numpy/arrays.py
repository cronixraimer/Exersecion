import numpy

def arrays(arr):
    #my_list = numpy.array(arr[::-1], float)
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
