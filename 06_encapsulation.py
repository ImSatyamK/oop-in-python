class Bank:
    def __init__(self):
        self.__balance = 500

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

bank = Bank()
print(bank.get_balance())  # Accessing balance via getter method
bank.deposit(200)
print(bank.get_balance())  # Balance after deposit
bank.withdraw(100)
print(bank.get_balance())  # Balance after withdrawal
# The following line would raise an AttributeError due to name mangling
# print(bank.__balance)  # Uncommenting this line will cause an error