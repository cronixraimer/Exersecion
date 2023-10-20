import re
s = input()
pattern = "(?<=[^aeiou])([aeiou]{2,})[^aeiou]"
x = re.findall(pattern, s, flags = re.I)

print("\n".join(x) if x else "-1")
