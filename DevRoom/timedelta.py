import time
from datetime import datetime, timedelta
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    t1_input = datetime.strptime(t1, format_string)
    t2_input = datetime.strptime(t2, format_string)
    value = abs(t1_input - t2_input)
    return str(int(value.total_seconds()))

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    print(delta + '\n')
