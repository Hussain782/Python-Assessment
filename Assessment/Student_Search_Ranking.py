students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 78
}

def find_student(students, name):
    name = name.lower()

    for student in students:
        if student.lower() == name:
            return {
            "name": student,
            "score": students[student],
            "status": "found"
        }

    return{
        "name": name,
        "score":  None,
        "status": "Not found"
        }

print(find_student(students, "charlie"))
print(find_student(students, "david"))
print(find_student(students, "bob"))
print(find_student(students, "John"))
print(find_student(students, "Ajay"))