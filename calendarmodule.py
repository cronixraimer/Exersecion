import calendar


mm, dd, yy = list(map(int, input().split(' ')))

n = calendar.day_name[calendar.weekday(yy,mm,dd)]

print(n.upper())
