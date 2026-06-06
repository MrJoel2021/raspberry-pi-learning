name = input("What is your name? ")
mark = int(input("What is your mark? "))

if mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 40:
    grade = "D"
else:
    grade = "F"

print(name, "got grade", grade)
