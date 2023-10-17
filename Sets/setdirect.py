class Friend:
    def __init__(self):
        self.job = "None"

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

    def getAge(self):
        return self.job

    def setAge(self, age):
        self.age = age



Alice = Friend()
Bob = Friend()

Alice.setJob("Cleaner")
Bob.setJob("Painter")

Alice.setAge("32 years old")
Bob.setAge("34 years old")

print(Bob.age)
print(Alice.age)

print(Bob.job)
print(Alice.job)
#two objects are created, both of them have unique value for the property job:

    #Friend
    #+Job+              Alice
    #+setJob(job) + getJob()    Bob
