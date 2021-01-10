# Grading Students

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38 or grade % 5 < 3:
            result.append(grade)

        elif grade % 5 >= 3:
            result.append(5 - (grade % 5) + grade)

    return result

grades = list(map(int, "73 67 38 33".split()))
result = gradingStudents(grades)
print(result)
