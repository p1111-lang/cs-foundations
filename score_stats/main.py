import statistics_utils
print("== Grade Calculation Program ==")
student_number = int(input("Enter student number: "))
if student_number <= 0:
    print("Please enter a positive integer for the number of students.")

grade = {}
for i in range(student_number):
    name = input("Enter name for student : ")
    score = float(input("Enter score for student : "))
    grade[name] = score

print("The average score is:", statistics_utils.calculate_average(grade))
print("The maximum score is:", statistics_utils.maximum(grade))
print("The minimum score is:", statistics_utils.minimum(grade))
passed_students, failed_students = statistics_utils.pass_fail(grade)
print("Passed students:")
for name, score in passed_students.items():
    print(f"{name}: {score}")
print("Failed students:")
for name, score in failed_students.items():
    print(f"{name}: {score}")
