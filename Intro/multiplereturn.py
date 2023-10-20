
def complexfunction(a, b):
    sum = a + b
    return sum

print("Sum of a + b = ",complexfunction(2, 3))


def getPerson():
    name = "Leo"
    age = 28
    country = "US"
    return name, age, country

name, age, country = getPerson()
print(name)
print(age)
print(country)
