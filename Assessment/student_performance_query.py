students = {
    "Alice": 85,
    "Charlie": 91,
    "Bob": 72,
    "David": 64,
    "Emma": 78 
}

def student_query(students, query):
    if query == "highest":
        highest_student = ""
        highest_score = 0

        for student in students:
            if students[student] > highest_score:
                highest_score = students[student]
                highest_student = student

        return {"highest_student_name": highest_student, 
                "highest_score": highest_score,
        }
    
    elif query == "lowest":
        first_student = list(students)[0]

        lowest_student = first_student
        lowest_score = students[first_student]

        for student in students:
            if students[student] < lowest_score:
                lowest_score = students[student]
                lowest_student = student

        return {"lowest_student_name": lowest_student,
                "lowest_score": lowest_score
        }
    elif query == "average":
         average_score = calculate_average(students)

         return{"average_score": average_score}
    
    elif query == "above_average":
            above_average = {}
            average_score = calculate_average(students)
            
            for student in students:
                if students[student] > average_score:
                    above_average[student] = students[student]

            return{"Above_average": above_average}

    elif query == "below_average":
            below_average = {}
            average_score = calculate_average(students)
            for student in students:
                if students[student] < average_score:
                    below_average[student] = students[student]

            return{"Below_average": below_average}

    else:
         return{"error": "Invalid_Query"}

def calculate_average(students):
            total_student = len(students)
            total_score = 0
            for student in students:
                total_score += students[student]
            if len(students) > 0:
                average_score = total_score / total_student
            else:
                 average_score = 0
            return average_score

def run_student_system(students):
    while True:

        print("\nStudent Analysis System")
        print("1. Highest student")
        print("2. Lowest student")
        print("3. Average score")
        print("4. Above average")
        print("5. Below average")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                print(student_query(students, "highest"))

            case "2":
                print(student_query(students, "lowest"))

            case "3":
                print(student_query(students, "average"))

            case "4":
                print(student_query(students, "above_average"))

            case "5":
                print(student_query(students, "below_average"))

            case "6":
                print("Goodbye!")
                break

            case _:
                print("INVALID CHOICE!")

print(run_student_system(students))