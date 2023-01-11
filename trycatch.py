
try:
    x = input("Enter number: ")
    x = x + 1
    print(x)
except:
    print("Invalid input")

def fail():
    1 / 0

try:
    fail()
except:
    print('Exception occured')

print('Program continues')
