response = input("Do you want to continue? ")

count = 0

while response.lower() == "yes":
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    average = (score1 + score2) / 2

    print("Last name:", last_name)
    print("Average:", average)

    count = count + 1

    response = input("Do you want to continue? ")

print("Number of students:", count)
