students = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 91,
        "David": 64,
        "Emma": 78
    }
def analyze_students(students):

    total_student = len(students)

    highest_score = 0
    for student in students:
        if students[student] > highest_score:
            highest_score = students[student]


    lowest_score = highest_score
    for student in students:
        if students[student] < lowest_score:
            lowest_score = students[student]

    total_score = 0
    for student in students:
        total_score += students[student]

    average_score = total_score / total_student



    return {"total_student": total_student,
            "highest_score": highest_score,
            "lowest_score": lowest_score,
            "total_score": total_score,
            "average_score": average_score
    }

print(analyze_students(students))
