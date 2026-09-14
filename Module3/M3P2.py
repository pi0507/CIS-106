last_name = input("Enter student last name: ")
midterm = float(input("Enter midterm exam score: "))
final_exam = float(input("Enter final exam score: "))

total = (midterm * 0.40) + (final_exam * 0.60)

print("Student:", last_name)
print(f"Total exam points: {total:.2f}")
