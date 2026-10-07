response = input("Do you want to continue? ")

total_discounts = 0

while response.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    extended_price = quantity * price

    if extended_price > 10000:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print("Extended price:", extended_price)
    print("Discount amount:", discount_amount)
    print("Total:", total)

    total_discounts = total_discounts + discount_amount

    response = input("Do you want to continue? ")

print("Total discounts:", total_discounts)
