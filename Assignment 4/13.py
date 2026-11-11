class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    def get_account_number(self):
        return self.__account_number
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
    def get_balance(self):
        return self.__balance
account = BankAccount("123456789", 5000)
print("Account Number:", account.get_account_number())
account.deposit(2000)
account.withdraw(1500)
print("Current Balance:", account.get_balance())
account.withdraw(10000)
account.deposit(-500)
print("Final Balance:", account.get_balance())