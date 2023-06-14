from datetime import datetime as dt
from Bank import Bank
from User import User

class Admin(User, Bank):
    def __init__(self, name, email, address, phone) -> None:
        super().__init__(name, email, address, phone)

    def create_account(self, user, initail_deposit):
        return super().create_account(user, initail_deposit)

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
            print(f"Loan Feature is Off {dt.now}")
        