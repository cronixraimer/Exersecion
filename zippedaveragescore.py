
#create and read map N of student X subject
N, X= map(int,input().split())

point = []

#iterating points on each sunject
for i in range(X):
    point.append(list(map(float, input().split(' '))))

#zipping each points of subject to score
score = list(zip(*point))

#iterating each subjects point to get avareage of score
for i in score:
    print(round(sum(i)/X, 1))
