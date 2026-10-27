print("how many numbers do you want to enter?")
num = int(input())
numbers = []
if num <= 0:
    print("Please enter a positive integer.")
for i in range(num):
    print("Enter number", i + 1, ":")
    number = float(input())
    numbers.append(number)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

print("The average of the numbers is:", calculate_average(numbers))
print("The maximum number is:", find_maximum(numbers))
print("The minimum number is:", find_minimum(numbers))
