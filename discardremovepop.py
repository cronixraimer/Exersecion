N = int(input())
my_set_n = set(map(int, input().split()))
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == "remove":
        my_set_n.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        my_set_n.discard(int(cmd[1]))
    elif cmd[0] =="pop":
         my_set_n.pop()
print(sum(my_set_n))
