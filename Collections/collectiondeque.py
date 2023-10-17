from collections import deque

#creatiing an empty input number of operation will be repetead
n_op = int(input())

#initiailazing deque
d = deque()

#number of operation will be repetead untill condition will not be met
for i in range(n_op):
    #creating an empty command for deque operation
     op = input().split()
     #checking if the input belongs to which command and condition will be met
     if op[0] == 'append':
         d.append(int(op[1]))
     elif op[0] == 'pop':
         d.pop()
     elif op[0] == 'popleft':
         d.popleft()
     elif op[0] == 'appendleft':
        d.appendleft(int(op[1]))

#initiailazing result to be printed
for op in d:
    print(op, end = " ")
