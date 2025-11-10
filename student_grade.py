
# grade.py
# Program: Exam Grade Calculator
# Description:
#   Prompts for a student's numeric score and prints
#   the corresponding letter grade using nested if/elif/else logic.

# Grading scale:
#   90–100 : A
#   80–89  : B
#   70–79  : C
#   60–69  : D
#   < 60   : F


student_score = int(input("Enter score: "))

if student_score >= 90:
    student_grade = "A"

elif student_score >= 80:
    student_grade = "B"

elif student_score >= 70:
    student_grade = "C"

elif student_score >= 60:
    student_grade = "D"

else:
    student_grade = "F"

print(f"{student_score} = {student_grade}")
