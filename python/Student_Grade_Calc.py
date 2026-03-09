#WAP to take a user input as number grade in following subjects and find out the division they secured.

Computer = float(input("Enter your grade in Computer subject:"))
Mathematics = float(input("Enter your grade in Mathematics subject:"))
Science = float(input("Enter your grade in Science subject:"))
English = float(input("Enter your grade in English subject:"))

Total = Computer + Mathematics + Science + English
Percentage = Total/4
gpa = (Percentage / 100) * 4.0

if Percentage >= 90:
    division = "A"
elif Percentage >= 70:
    division = "B"
elif Percentage >= 60:
    division = "C"
elif Percentage >= 50:
    division = "D"
elif Percentage >= 40:
    division = "E"
else:
    division = "FL"

print(f"Your total grade is: {Total}")
print(f"Your percentage is: {Percentage}%")
print(f"Your GPA is: {gpa}")
print(f"Your division is: {division}")
