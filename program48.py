
class BankAccount:
    def initialize(self):
        self.name = input("Enter depositor name: ")
        self.account_number = input("Enter account number: ")
        self.account_type = input("Enter account type: ")
        self.balance = float(input("Enter initial balance: "))

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n--- Bank Account Details ---")
        print("Depositor name:", self.name)
        print("Account number:", self.account_number)
        print("Account type:", self.account_type)
        print("Available balance:", self.balance)


account = BankAccount()
account.initialize()
account.deposit()
account.withdraw()
account.display()

