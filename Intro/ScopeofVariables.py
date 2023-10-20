def sample():
    localVar = 1

#this will crash because localVar is a local variabl print(localVar)

#global and local variables

balance = 0

def addAmount(x):
    global balance
    balance = balance + x

addAmount(5)
print(balance)

#balance = 0 global variable -> addAmount(x) -> use gobal variable balance
#                                            -> x only known inside funcntion which is local variable
currentbalance = 25
def reduceAmount(y):
    global currentbalance
    currentbalance = currentbalance - y

reduceAmount(10)
print(currentbalance)
