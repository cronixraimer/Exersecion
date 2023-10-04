from collections import OrderedDict

inventory = OrderedDict()

n = int(input())

for i in range(n):
    item_bought = input().split()
    net_price = int(item_bought[-1])
    item_name = " ".join(item_bought[0:-1])
    if item_name in inventory:
        inventory[item_name] += net_price
    else:
        inventory[item_name] = net_price

for key, value in inventory.items():
    print(key, value)
