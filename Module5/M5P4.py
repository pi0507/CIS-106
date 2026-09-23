appliance_name = input("Enter appliance name: ")
appliance_cost = float(input("Enter appliance cost: "))

if appliance_cost > 1000:
    warranty_cost = appliance_cost * 0.10
else:
    warranty_cost = appliance_cost * 0.05

total = appliance_cost + warranty_cost

print("Appliance Name:", appliance_name)
print("Appliance Cost: $", format(appliance_cost, ".2f"))
print("Warranty Cost: $", format(warranty_cost, ".2f"))
print("Total Cost: $", format(total, ".2f"))
