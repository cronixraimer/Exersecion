import numpy

n, m = map(int, input().split())

my_list = []

for i in range(n):
    my_list.append(list(map(int, input().split())))

t = numpy.array(my_list)
print(numpy.transpose(t))
print(t.flatten())
