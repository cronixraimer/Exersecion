#read otertools.permutation library then solve problem
from itertools import permutations

def lexicographic(s, n):
    for i in permutations(s, n):
        print(*i, sep = '')




first_multiple_input = input().split()

s = sorted(first_multiple_input[0])

n = int(first_multiple_input[1])

result = lexicographic(s, n)
