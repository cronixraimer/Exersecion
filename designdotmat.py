
mode = input().split()
rows  = int(mode[0])
columns = int(mode[1])
h = '-'
t = '.|.'

#Head
for i in range(0, rows//2):
    print((t * i).rjust((columns - 3)//2,h) + t + (t * i).ljust((columns - 3 )//2,h))

#Center Welcome word
print('WELCOME'.center(columns,h))

#Bottom
for i in range(0, rows//2):
    print((t*((rows - 1)//2 - i - 1)).rjust((columns - 3)//2,h) + t + (t * ((rows - 1)//2 - i - 1)).ljust((columns - 3)//2,h))
