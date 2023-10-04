from collections import namedtuple

num_student = int(input())

columns = input().split()

Students = namedtuple('Students', columns)

s = 0

for i in range(num_student):
    data = input().split()
    student = Students(*data)
    s = s + int(student.MARKS)
print(s/n)
