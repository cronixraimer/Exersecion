def average(array):
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#the sum of the unique elements using sum(set(array)) and divides it
# by the number of unique elements, len(set(array)), to compute the average.
#prompts the user to enter n space-separated integers using input() and split(),
#and converts them to integers using map(int, ...).
