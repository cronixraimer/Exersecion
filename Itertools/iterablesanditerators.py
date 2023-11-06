import itertools

n = int(input())

k = input().split()

d = list(itertools.combinations(k, int(input())))

formatted_list = [i for i in d if "a" in i]

t = len(formatted_list) / len(d)

print(formatted_list)
print(d)
print(round (t, 3))
