from datetime import datetime as dt
from User import User

class Admin(User):
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.type = "Admin"
        self.activity_log = []

    def create_account(self, bank, email, phone, address):
        return super().create_account(bank, email, phone, address)


    def total_available_balance(self, bank):
        if self.name in bank.admins:
            print(bank.get_balance)
        else:
            print(f"Admin not Authorized to get access of {bank.name}")
    
    def total_loan_amount(self, bank):
        if self.name in bank.admins:
            print(bank.get_loan_balance)
        else:
            print(f"Admin not Authorized to get access of {bank.name}")
    
    def switch_loan_feature(self, switch):
        if switch == True:
            super().loan_enabled = True
            print(f"Loan Feature is On {dt.now}")
        else:
            super().loan_enabled = False
            print(f"Loan Feature is ff {dt.now}")

    