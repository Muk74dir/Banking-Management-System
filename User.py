from datetime import datetime as dt

class User:
    def __init__(self, name, email, address, phone) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.phone = phone
        self.balance = 0
        self.activity_log = []


    def deposit(self, amount):
        self.balance += amount
        self.activity_log.append(f'Credited +{amount} at {dt.now()}')
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.activity_log.append(f'Debited -{amount} at {dt.now()}')
            print("Withdraw Successful.")
        else:
            print("Not Enough Money Available to Withdraw.")
            

    def check_balance(self):
        print(f'Your Balance is : {self.balance}')

    def transfer_balance(self, to_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            to_user.balance += amount
            self.activity_log.append(f'{amount}BDT Transfered from {self.name} to {to_user.name} at {dt.now()}')
            print("Transfer Successful.")
        else:
            print("Not Enough Money Available to Transfer.")


    def transaction_history(self):
        for activity in self.activity_log:
            print(activity)
