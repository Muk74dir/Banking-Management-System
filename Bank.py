from datetime import datetime as dt

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__balance = 0
        self.__loan = 0
        self.users = {}
        self.admins = {}
        self.loan_enabled = True

        print(f"##########---------->WELCOME TO {self.name}<---------#######\n\n\n")


    @property
    def get_balance(self):
        return self.__balance
    
    @get_balance.setter
    def get_balance(self, amount):
        self.__balance = amount
    

    @property
    def get_loan_balance(self):
        return self.__loan
    
    @get_loan_balance.setter
    def get_loan_balance(self, amount):
        self.__loan = amount


    def is_loan_enabled(self):
        return self.loan_enabled

    def total_balance(self):
        return self.get_balance
    
    def total_loan(self):
        return self.get_loan

    def account_details(self, user):
        print("<----------Account Details-------->")
        print(f'Account Name : {user.name}')
        print(f'Account Type : {user.type}')
        print(f'{user.type} Phone Number : {user.phone}')
        print(f'{user.type} email : {user.email}')
        print(f'{user.type} address : {user.address}')
        print(f'{user.type} Balance : {user.balance}\n\n')

        




