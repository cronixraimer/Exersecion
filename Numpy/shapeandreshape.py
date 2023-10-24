import numpy

def arrays(arr):

    return numpy.reshape(arr,(3,3))


arr = list(map(int, input().split()))
result = arrays(arr)
print(result)
