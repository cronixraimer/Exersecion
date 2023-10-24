import numpy

n, m, p = map(int, input().split())

my_list = []

for i in range(n + m):
    my_list.append(list(map(int, input().split())))

print(numpy.array(my_list))
