students = {
    "Alice": 85,
    "Bob": 72,
    "David": 64,
    "Charlie": 91,
    "Emma": 78
}

def statistics_analyzer(students):
    total_student = len(students)

    excellent = 0
    very_good = 0
    good = 0
    passed = 0
    failed = 0

    largest_group = ""
    largest_count = 0

    smallest_group = ""
    smallest_count = total_student
    for student in students:
        if students[student] >= 90:
            excellent += 1

        elif students[student] >= 80:
            very_good += 1

        elif students[student] >= 70:
            good += 1

        elif students[student] >= 60:
            passed += 1

        else:
            failed += 1

        excellent_percentage = (excellent / total_student) * 100
        very_good_percentage = (very_good / total_student) * 100
        good_percentage = (good / total_student) * 100
        passed_percentage = (passed / total_student) * 100
        failed_percentage = (failed / total_student) * 100

    if excellent > largest_count:
            largest_count = excellent
            largest_group = "Excellent"

    if very_good > largest_count:
            largest_count = very_good
            largest_group = "Very_good"

    if good > largest_count:
            largest_count = good
            largest_group = "Good"

    if passed > largest_count:
            largest_count = passed
            largest_group = "Passed"

    if failed > largest_count:
            largest_count = failed
            largest_group = "Failed"

    if excellent < smallest_count:
            smallest_count = excellent
            smallest_group = "Excellent"

    if very_good < smallest_count:
            smallest_count = very_good
            smallest_group = "Very_good"

    if good < smallest_count:
            smallest_count = good
            smallest_group = "Good"

    if passed < smallest_count:
            smallest_count = passed
            smallest_group = "Passed"

    if failed < smallest_count:
            smallest_count = failed
            smallest_group = "Failed"
    
    return {
            "Excellent": excellent,
            "Excellent-percentage": excellent_percentage,
            "Very-Good": very_good,
            "Very-good-percentage": very_good_percentage,
            "Good": good,
            "Good-percentage": good_percentage,
            "Passed": passed,
            "Passed-percentage": passed_percentage,
            "Failed": failed,
            "Failed-percentage": failed_percentage,
            "largest_group": largest_group,
            "largest_count": largest_count,
            "smallest_group": smallest_group,
            "smallest_count": smallest_count
        }

print(statistics_analyzer(students))