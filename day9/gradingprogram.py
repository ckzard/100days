student_scores = {

    "Harry" : 81,
    "Ron" : 70,
    "Hermione" : 99,
    "Draco" : 85,
    "Neville" : 78

}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)