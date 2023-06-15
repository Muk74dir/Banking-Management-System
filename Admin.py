from datetime import datetime as dt
from Bank import Bank
from User import User

class Admin(User, Bank):
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.type = "Admin"
        self.activity_log = []

    def create_account(self, bank, email, phone, address):
        return super().create_account(bank, email, phone, address)


    def total_available_balance(self):
        return super().get_balance
    
    def total_loan_amount(self):
        return super().get_loan
    
    def switch_loan_feature(self, switch):
        if switch == True:
            super().loan_enabled = True
            print(f"Loan Feature is On {dt.now}")
        else:
            super().loan_enabled = False
            print(f"Loan Feature is ff {dt.now}")

    