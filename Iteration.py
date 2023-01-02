city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

print('\n')  # newline

num = [1,2,3,4,5,6,7,8,9]
num2 = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))


clist = ['Canada', 'USA', 'Mexico', 'Australia']
print('Clist: ')

for x in clist:
    print('Clist: ' + x)

print('\n')

for x in range(101):
    print(x)

for x in num:
    for y in num2:
        z = x * y
        print(str(x) + '*' + str(y) + '=' + str(z))


for x in range(10, 0, -1):
    print(x)

for x in range(10, 0, -1):
     if x % 2 == 0:
         print(x)

for x in range(100, 200):
    y = x + x
    print(y)
