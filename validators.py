s = input()
list = list(s)
alnum = False
alpha = False
digit = False
lower = False
upper = False
for i in list:
    alpha = alpha or i.isalpha()
    digit = digit or i.isdigit()
    lower = lower or i.islower()
    upper = upper or i.isupper()
alnum = alpha or digit
print(f"{alnum}\n{alpha}\n{digit}\n{lower}\n{upper}")
