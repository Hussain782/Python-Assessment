students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 78
}

def generate_report(students, passing_score):
    total_students = len(students)

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

    average_score = total_score / total_students

    passed_students = {}
    for student in students:
        if students[student] >= passing_score:
            passed_students[student] = students[student]

    passed_count = len(passed_students)

    return {"Total_students": total_students,
            "Highest_Score": highest_score,
            "Lowest_Score": lowest_score,
            "Total_Score": total_score,
            "Average_Score": average_score,
            "Passed_students": passed_students,
            "Passed_count": passed_count
            }
print(generate_report(students, 80))