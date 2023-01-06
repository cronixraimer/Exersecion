
persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    for restautrant in restaurants:
        print(person + " eats " + restautrant + " food")


#given a tic tac toe board of 3x3 print every postion
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw():

        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

draw()

for i in persons:
    for j in persons:
        print(i + '-> ' + j)
