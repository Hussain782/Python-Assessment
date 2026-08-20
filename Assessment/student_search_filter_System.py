students = {
    "Alice": 85,
    "Bob": 72,
    "David": 64,
    "Charlie": 91,
    "Emma": 78
}

def student_filter(students, minimum_score):
    filtered_students = {}
    for student in students:
        if students[student] >= minimum_score:
            filtered_students[student] = students[student] 

    count = len(filtered_students)

    total_score = 0
    for student in filtered_students:
        total_score += filtered_students[student]

    if len(filtered_students) > 0:
        average_score = total_score / count

    else:
        average_score = 0

    highest_student = ""
    highest_score = 0
    for student in filtered_students:
        if filtered_students[student] > highest_score:
            highest_score = filtered_students[student]
            highest_student = student

    lowest_student = highest_student
    lowest_score = highest_score
    for student in filtered_students:
            if filtered_students[student] < lowest_score:
                lowest_score = filtered_students[student]
                lowest_student = student

    return {
    "filtered_students": filtered_students,
    "Count": count,
    "average_score": average_score,

    "highest_student": {
        "name": highest_student,
        "score": highest_score
    },

    "lowest_student": {
        "name": lowest_student,
        "score": lowest_score
    }
}

print(student_filter(students, 75))