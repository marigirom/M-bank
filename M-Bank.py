# bankAccount class
class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Ksh{amount} successfuly deposited! New balance:Ksh{self.balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Ksh{amount} withdrawn successfully! New balance:{self.balance}")
        else:
            print("Insufficient balance or invalid amount!!")

    def get_balance(self):
        return self.balance
    
#Savings

class SavingsAccount(BankAccount):
    
    def __init__(self, account_holder, balance=0,interest_rate = 0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest:Ksh{interest}> New balance:Ksh{self.balance}")

# Checkingacoount class

class CheckingAccount(BankAccount):
    
    def __init__(self, account_holder, balance=0, limit = 200):
        super().__init__(account_holder, balance)
        self.limit =limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.limit:
            self.balance -= amount
            print(f"Ksh{amount} withdrawn successfully. New balance:Ksh{self.balance}")
        else:
            print("withdrawal exceeds the limit!!")


# instance BankAccount
account1 = BankAccount("Mary Too", 2000)
account1.deposit(500)
account1.withdraw(200)
print(f"Current Balance:Ksh{account1.get_balance()}")

# instance savingsAccount
savings = SavingsAccount("Lucy", 1500)
savings.add_interest()
savings.deposit(50)
savings.withdraw(20)

# checking

checking = CheckingAccount("Job", 400)
checking.withdraw(500)



 