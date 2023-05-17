if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = []
    for student, grade in records:
        scores.append(grade)

    second_lowest = sorted(set(scores))[1]

    for student, grade in sorted(records):
        if grade == second_lowest:
            print(student)
