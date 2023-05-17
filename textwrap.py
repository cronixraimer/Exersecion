import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), input()
    result = wrap(string, max_width)
    print(result)
#note on cmd it was given erroe as library of wrap is not installed on laptop!!!
