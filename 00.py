

class BankAccount:
    def __init__(self, account_number, user_name, balance=0, loan_limit=0):
        self.account_number = account_number
        self.user_name = user_name
        self.balance = balance
        self.loan_limit = loan_limit
        self.transactions = []


    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")


    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred: {amount} to {recipient.user_name}")
        else:
            print("Insufficient funds")


    def take_loan(self, amount):
        if amount <= self.loan_limit:
            self.balance += amount
            self.loan_limit -= amount
            self.transactions.append(f"Loan taken: {amount}")
        else:
            print("Loan limit exceeded")


    def show_balance(self):
        return self.balance


    def show_transactions(self):
        return self.transactions



class Bank:
    def __init__(self):
        self.accounts = []


    def create_account(self, account_number, user_name, balance=0, loan_limit=0):
        account = BankAccount(account_number, user_name, balance, loan_limit)
        self.accounts.append(account)
        return account


    def total_balance(self):
        return sum(account.balance for account in self.accounts)


    def total_loan_amount(self):
        return sum(account.loan_limit for account in self.accounts)


    def enable_loan_feature(self):
        for account in self.accounts:
            account.loan_limit = account.show_balance() * 2


    def disable_loan_feature(self):
        for account in self.accounts:
            account.loan_limit = 0




bank = Bank()




user1 = bank.create_account("1001", "Alice", balance=1000)
user2 = bank.create_account("1002", "Bob", balance=1500)




user1.deposit(500)
user2.deposit(1000)



user1.transfer(user2, 300)
user2.withdraw(700)



user1.take_loan(200)
user2.take_loan(300)




print(user1.show_balance())
print(user2.show_transactions())




admin = BankAccount("admin", "Admin")
admin_account = bank.create_account(admin.account_number, admin.user_name)



admin_account.deposit(50000)
print(bank.total_balance())
print(bank.total_loan_amount())



bank.enable_loan_feature()
user1.take_loan(400)
print(user1.show_balance())









