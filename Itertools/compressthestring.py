from itertools import groupby

user_input = input()

groups = [(key, list(group)) for key, group in groupby(user_input)]

formatted_groups = [f'({len(group)}, {key})' for key, group in groups]

print(' '.join(formatted_groups))
