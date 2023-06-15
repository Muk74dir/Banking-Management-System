from datetime import datetime as dt
from Bank import Bank

class User:
    def __init__(self, name) -> None:
        self.name = name 
        self.balance = 0
        self.activity_log = []
        self.type = "User"

    def create_account(self, bank, email, phone, address):
        self.email = email
        self.phone = phone
        self.address = address

        if self.type == "User":
            print("######----User Account Created---#####\n")
            bank.users[self.name] = self
        else:
            print("######----Admin Account Created---#####\n")
            bank.admins[self.name] = self
        self.activity_log.append(f'Account Created at {dt.now()}')

    def deposit(self, bank, amount):
        self.balance += amount
        self.activity_log.append(f'Credited +{amount} in {bank.name} at {dt.now()}')
        bank.get_balance += amount
        
    def withdraw(self, bank, amount):
        if self.balance >= amount:
            self.balance -= amount
            bank.get_balance -= amount
            self.activity_log.append(f'Debited -{amount} from {bank.name} at {dt.now()}')
            print("Withdraw Successful.")
        else:
            print("Not Enough Money Available to Withdraw.")
            

    def check_balance(self, bank):
        if self.name in bank.users:
            print(bank.users[self.name].balance)
        else:
            print(f"No Account Found for user : {self.name} in {bank.name}")
        

    def transfer_balance(self, bank, to_user, amount):
        if (self.name in bank.users) and (to_user.name in bank.users):
            if self.balance >= amount:
                self.balance -= amount
                to_user.balance += amount
                self.activity_log.append(f'{amount}BDT Transfered from {self.name} to {to_user.name} at {dt.now()}')
                print(f"Transfer Successful from {self.name} to {to_user.name} by {bank.name}")
            else:
                print("Not Enough Money Available to Transfer.")
        else:
            print("Transfer Failed")
            print('Reason : User has no account in this bank')


    def transaction_history(self):
        for activity in self.activity_log:
            print(activity)
