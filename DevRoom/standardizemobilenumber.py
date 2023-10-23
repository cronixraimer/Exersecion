import re
def wrapper(f):
    p = re.compile(r'^\+?(91)?(0)?(?P<number>\d{10})$')
    def fun(l):

        formatted_numbers = []

        for i in l:
            number = p.match(i)['number']
            if number:
                formatted_numbers.append(f'+91 ' + number[:5] + ' ' + number[5:])
        f(formatted_numbers)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
