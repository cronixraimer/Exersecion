x = int(input())

for i in range(x):
    a, b = input().split()

    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as v:
        print('Error Code:', v)
