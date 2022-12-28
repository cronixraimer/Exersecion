x = 3
if x < 10:
    print('x below ten')

y = 11
if y > 10:
    print('y is greater than ten')
z = 2
if z > 1 and z < 4:
    print('z is in range')

gender = input("Your Gender? ")
gender = gender.lower()

if gender == "male":
    print("Your cat is male")
elif gender == "female":
    print("Your cat is female")
else:
    print("Invalid input")

    age = int(input("Age of your cat? "))
    if age < 5:
        print("Your cat is young.")
    else:
        print("Your cat is adult.")

# password = string(input("please write down your password"))

number = int(input("Please chose the number between 1 to 10 "))

if number > 1 and number < 10:
    print("Your number is on range")
else:
    print("invalid number")
