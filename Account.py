class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        """Base withdraw method can be overwritten by the subclasses"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.withdraw_limit = 100
        
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print("Amount exceeds the $100 withdrawal limit.")
        else:
            super().withdraw(amount)
