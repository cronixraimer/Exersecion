for i in range(1, 11): #difine simple range from 1 to 10
    print(i)
for i in range(0, 25, 5): #deifine step by size which is by 5
    print(i)
#get largest and smallest number from the list

x = list(range(1, 50))
print(min(x))
print(max(x))

#an even and odd from the list

for i in x:
    if i % 2 == 0:
        print(i)
        print('\n')
    else:
        print(i)
