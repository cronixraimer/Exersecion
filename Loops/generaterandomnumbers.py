import random

print(random.random())

print(random.randrange(0, 10))

print(random.uniform(0, 10))

x = random.uniform(1, 100)
y = random.uniform(1, 100)
z = random.uniform(1, 100)
print(x, y , z)

n = random.sample(range(0, 10), 10)
print(n)

mylist = [n]
newlist = []
duplist = []

for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)

print(duplist)
print(newlist)
