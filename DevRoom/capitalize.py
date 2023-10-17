# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    return " ".join([i.capitalize() for i in s])


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
