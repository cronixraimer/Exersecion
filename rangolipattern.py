import string
def print_rangoli(size):


    characters = string.ascii_lowercase
    lines = []
#the lines of the pattern
    for i in range(size):
        line = '-'.join(characters[i:size])
        lines.append((line[::-1] + line[1:]).center(4 * size - 3, '-'))

#the pattern in reverse order

    for line in reversed(lines):
        print(line)

#the remainig lines in normal order
    for line in lines[1:]:
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
