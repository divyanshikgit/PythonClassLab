students = input("Enter the number of students")   # Take the input from he User
students = int(students)
feet = []
cm = []
for n in range(students):
    r = float(input("Enter the height in foot: "))      # Take the decimal values as well of height
    feet.append(r)

cm = [feet[f] * 30.48 for f in range(students)]     # Convert the feet to cm

print("The heights of the students in cms is  ", cm)