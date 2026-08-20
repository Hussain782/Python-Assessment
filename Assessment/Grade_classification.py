students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 78
}

def classify_student(students):
    grades = {}
    grade_count = {}

    for student in students:
        if students[student] >= 90:
            grade = "A"

        elif students[student] >= 80:
            grade = "B"

        elif students[student] >= 70:
            grade = "C"

        elif students[student] >= 60:
            grade = "D"

        else:
            grade = "F"

        grades[student] = grade

        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1

    return grades, grade_count

print(classify_student(students))