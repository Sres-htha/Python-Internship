# Create a class Bank Account and perform specified methods
class BankAccount:
    def __init__(self, account_number, account_holder, balance):   #Initialise the attributes
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):          # Add money to the balance
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount}. New balance is Rs {self.balance}.")
        else:
            print("Deposit amount must be positive.")              # Amount cannot be negative

    def withdraw(self, amount):              # Subtract money from the balance
        if amount > 0:
            if amount <= self.balance: 
                self.balance -= amount
                print(f"Withdrew Rs {amount}. New balance is Rs {self.balance}.")
            else:
                print("Insufficient account balance.")             # balance needs to be grater than amount
        else:
            print("Withdrawal amount must be positive.")           # Amount cannot be negative

    def get_balance(self):          
        return self.balance

# Input:
account = BankAccount("123456789", "Michael", 1000.0)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: Rs {account.get_balance()}")
