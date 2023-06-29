n = int(input())

available_size = list(map(int, input().split()))

t = int(input())

chosen_size = []


for i in range(t):
    chosen_size.append(list(map(int, input().split())))

revenue = 0

for chosen in chosen_size:
    chosen_size = chosen[0]
    price = chosen[1]

    if chosen_size in available_size:
        revenue += price
        available_size.remove(chosen_size)

print(revenue)
