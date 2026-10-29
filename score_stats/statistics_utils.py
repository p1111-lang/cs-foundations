def calculate_average(grade):
    return sum(grade.values()) / len(grade)

def maximum(grade):
    return max(grade.values())

def minimum(grade):
    return min(grade.values())

def pass_fail(grade):
    passed_students = {name: score for name, score in grade.items() if score >= 60}
    failed_students = {name: score for name, score in grade.items() if score < 60}
    return passed_students, failed_students

if __name__ == "__main__":
    print("== Grade Calculation Program ==")
    student_number = int(input("Enter student number: "))
    if student_number <= 0:
        print("Please enter a positive integer for the number of students.")
    else:
        grade = {}
        for i in range(student_number):
            name = input("Enter name for student : ")
            score = float(input("Enter score for student : "))
            grade[name] = score

        print("The average score is:", calculate_average(grade))
        print("The maximum score is:", maximum(grade))
        print("The minimum score is:", minimum(grade))
        passed_students, failed_students = pass_fail(grade)
        print("Passed students:")
        for name, score in passed_students.items():
            print(f"{name}: {score}")
        print("Failed students:")
        for name, score in failed_students.items():
            print(f"{name}: {score}")