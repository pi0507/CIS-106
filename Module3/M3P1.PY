ticker = input("Enter stock ticker symbol: ")
shares = int(input("Enter number of shares: "))
cost = float(input("Enter cost per share: $"))

amount = shares * cost

print("Stock ticker:", ticker)
print(f"Amount invested: ${amount:.2f}")
