# Class: BankAccount
# Create a class BankAccount with name and balance.
# Add methods:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Make sure withdrawal doesn't allow balance to go below 0.

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self):
        print(f"{self.balance} is the deposited amount")
    def withdraw(self):


    def get_balance(self):

amt=BankAccount('kalpna',20000)