make = input("Enter car make: ")
model = input("Enter car model: ")
msrp = float(input("Enter MSRP: $"))
discount_percent = float(input("Enter discount percentage: "))

discount = msrp * (discount_percent / 100)
final_price = msrp - discount

print("Car:", make, model)
print(f"Discount amount: ${discount:.2f}")
print(f"Final price: ${final_price:.2f}")
