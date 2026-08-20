students = {
    "Alice": 85,
    "Bob": 72,
    "David": 64,
    "Charlie": 91,
    "Emma": 78
}

def student_ranking(students):
    ranking = {}
    remaining_students = students.copy()
    rank = 1

    while len(remaining_students) > 0:
        highest_student = ""
        highest_score = 0

        for student in remaining_students:
            if remaining_students[student] > highest_score:
                highest_student = student
                highest_score = remaining_students[student]

        ranking[rank] = {
            "name": highest_student,
            "score": highest_score
        }

        rank += 1
        remaining_students.pop(highest_student)

    # print(ranking)
    # highest_student = ""
    # highest_score = 0
    # for student in students:
    #     if students[student] > highest_score:
    #         highest_student = student
    #         highest_score = students[student]

    # lowest_student = highest_student
    # lowest_score = highest_score
    # for student in students:
    #     if students[student] < lowest_score:
    #         lowest_student = student
    #         lowest_score = students[student]

    return ranking

def find_rank(ranking, name):
    for rank in ranking:
        if ranking[rank]["name"] == name:
            return rank

    return "Not Found"

print(student_ranking(students))
print(find_rank(student_ranking(students), "John"))
