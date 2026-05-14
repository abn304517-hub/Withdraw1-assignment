from Account import Account

class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02  # Example interest rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

# Test the Savings account
print("---Savings Account---")
savings = Savings("Alice", 1000)
print(f"Initial balance: {savings.get_balance()}")
savings.deposit(500)
savings.withdraw(200)
savings.apply_interest()

