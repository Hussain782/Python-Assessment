students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 78
}

def get_top_students(students, passing_score):
    top_students = {}

    for student in students:
        if students[student] >= passing_score:
            top_students[student] = students[student]

    total_score = 0
    for student in top_students:
        total_score += top_students[student]


    # average_score = total_score / len(top_students)

    if len(top_students) > 0:
        average_score = total_score / len(top_students)
    else:
        average_score = 0

    top_count = len(top_students)


    return {"Student": top_students,
            "Count": top_count,
            "average_score": average_score}

print(get_top_students(students, 100))