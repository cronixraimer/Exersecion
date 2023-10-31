from collections import Counter

user_input = input()

groups = sorted(list(user_input))


formatted_groups = Counter(groups).most_common(3)

for key, group in formatted_groups:
    print(key, group)
