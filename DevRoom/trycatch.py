
#try:
#    x = input("Enter number: ")
#    x = x + 1
#    print(x)
#except:
#    print("Invalid input")

#def fail():
#    1 / 0

#try:
#    fail()
#except:
#    print('Exception occured')

#print('Program continues')

try:
    x = 1
except:
    print('Failed to set x ')
else:
    print('No Exception occured ')
finally:
    print('We always do this')


def lunch():
    1 / 1

try:
    lunch()
except SyntaxError:
    print('Fix your syntax')
except TypeError:
    print('Oh no! A TypeError has occured')
except ValueError:
    print('A ValueError occured!')
except ZeroDivisionError:
    print('Did by zero?')
else:
    print('No exception')
finally:
    print('Ok then')

# raise MemoryError("Out of memory")

# raise ValueError("Wrong value")


class luncherror(Exception):
    pass

# raise luncherror("Programmer went to lunch")

class nomenyexception(Exception):
    pass

class outofbudget(Exception):
    print("Your balance is runnig out of budget")

balance = int(input("Enter a balance: "))
if balance < 1000:
    raise nomenyexception
elif balance > 10000:
    raise outofbudget
