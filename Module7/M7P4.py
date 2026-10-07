response = input("Do you want to continue? ")

count = 0
total_gross_pay = 0

while response.lower() == "yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    if hours > 40:
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross_pay = hours * rate

    print("Last name:", last_name)
    print("Gross pay:", gross_pay)

    total_gross_pay = total_gross_pay + gross_pay
    count = count + 1

    response = input("Do you want to continue? ")

print("Total gross pay:", total_gross_pay)
print("Number of employees:", count)

if count > 0:
    average_pay = total_gross_pay / count
    print("Average pay:", average_pay)
