# Grade Calculator Program
# Task 3: Conditional Statements & Logical Flow

# Take marks input from the user
marks = int(input("Enter your marks (0-100): "))

# Check for invalid marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

# Grade calculation using if-elif-else and logical operators
elif marks >= 90 and marks <= 100:
    print("Grade: A+")
    print("Performance: Excellent")

elif marks >= 80 and marks < 90:
    print("Grade: A")
    print("Performance: Very Good")

elif marks >= 70 and marks < 80:
    print("Grade: B")
    print("Performance: Good")

elif marks >= 60 and marks < 70:
    print("Grade: C")
    print("Performance: Average")

elif marks >= 50 and marks < 60:
    print("Grade: D")
    print("Performance: Needs Improvement")

else:
    print("Grade: F")
    print("Performance: Fail – Work Hard")