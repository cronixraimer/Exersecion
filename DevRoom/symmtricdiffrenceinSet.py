
sizex = int(input())
my_set_x = set(map(int, input().split()))
sizey = int(input())
my_set_y = set(map(int, input().split()))

M  = set(my_set_x.difference(my_set_y))
N = set(my_set_y.difference(my_set_x))
mylist = sorted(M.union(N))
for i in mylist:
    print(i)
