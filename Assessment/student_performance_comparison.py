students = {
    "Alice": 85,
    "Bob": 72,
    "David": 64,
    "Charlie": 91,
    "Emma": 78
}

def performance_comparison(students):
    above_average = {}
    below_average = {}
    equal_average = {}

    total_score = 0
    for student in students:
        total_score += students[student]

    average_score = total_score / len(students)

    for student in students:
        if students[student] > average_score:
            above_average[student] = students[student]

    for student in students:
        if students[student] < average_score:
            below_average[student] = students[student]

    above_count = len(above_average)
    below_count = len(below_average)

    highest_student = ""
    highest_score = 0

    for student in above_average:
        if above_average[student] > highest_score:
            highest_score = above_average[student]
            highest_student = student

    for student in students:
        if students[student] == average_score:
            equal_average[student] = students[student]


    return{
        "average_score": average_score,
        "above_average": above_average,
        "below_average": below_average,
        "above_count": above_count,
        "below_count": below_count,
        "Highest_student": highest_student,
        "Highest_Score": highest_score,
        "equal_average": equal_average
    }

print(performance_comparison(students))