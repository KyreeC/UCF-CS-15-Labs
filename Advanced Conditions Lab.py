grade = int(input("Enter a grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
elif grade >= 0:
    print("F")
else:
    print("ERROR: Grades cannot be negative numbers or words.")
