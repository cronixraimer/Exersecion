class Human:
    def __init__(self):
        self.legs = 2
        self.arms = 2

bob = Human()
print(bob.legs)

class Plane:
    def __init__(self):
        self.wings = 2
        #fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
        print('Accelerating')

    def flaps(self):
        print('Changing flaps')

    def wheels(self):
        print('Closing wheels')

b = Plane()


class Bug:
    def __init__(self):
        self.wings = 4

tom = Bug()

print(tom.wings)
print(bob.arms)

class Car:
    def __init__(self):
        self.wheels = 4
        self.rudder()
        self.driving()

    def rudder(self):
        print('Rudder only one and human on driving')

    def driving(self):
        print('Bob is driving a car with a speed of 60 km/h')

x = Car()
