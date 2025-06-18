# ATM Cash Withdrawal Validator
# Ask user for amount to withdraw.
# Must be a multiple of 100.
# Must not exceed ₹10,000.
# Must not be more than current balance (assume ₹8,500).
# Print suitable message using if, elif, else.
amount=int(input("Enter the amount you want to withdraw:"))
balance = 8500
if amount % 100 != 0:
    print("Amount must be a multiple of ₹100.")
elif amount > 10000:
    print("Amount must not exceed ₹10,000.")
elif amount > balance:
    print("Amount must not be more than current balance of ₹8,500.")
else:
    balance -= amount
    print(f"Withdrawal successful! New balance is ₹{balance}.")
