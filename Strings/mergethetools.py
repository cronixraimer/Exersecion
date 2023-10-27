def merge_the_tools(string, k):

    x = ""
    for i in range(0, len(string)):
        if string[i] not in x:
            x = x + string[i]
        if (i + 1) % k == 0:
            print(x)
            x = ""
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
