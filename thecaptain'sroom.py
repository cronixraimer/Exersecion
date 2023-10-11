from collections import Counter

K = int(input())

my_list = input().split()

#my_list = list(S)

element_count = Counter(my_set)


# Iterate through the set and count occurrences
#for num in my_set:
#    if num in element_count:
#        element_count[num] += 1
#    else:
#        element_count[num] = 1

# Find the unique integer

for num, count in element_count.items():
    if count == 1:
        # Print the unique integer
        print(num)
