total = float(input("Enter meal total: "))

tip15 = total * 0.15
tip18 = total * 0.18
tip20 = total * 0.20

print("With 15% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with Tip {total + tip15:.2f}")

print()

print("With 18% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with Tip {total + tip18:.2f}")

print()

print("With 20% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with Tip {total + tip20:.2f}")
