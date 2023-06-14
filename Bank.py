from datetime import datetime as dt

class Bank:
    def __init__(self) -> None:
        self.__balance = 0
        self.__loan = 0
        self.users = []
        self.admins = []
        self.loan_enabled = True


    @property
    def get_balance(self):
        return self.__balance
    

    @property
    def get_loan(self):
        return self.__loan


    def is_loan_enabled(self):
        return self.loan_enabled

    def total_balance(self):
        return self.get_balance
    
    def total_loan(self):
        return self.get_loan

    def create_account(self, user):
        user.activity_log.append(f'Account Created at {dt.now()}')
        if user.type == "User":
            self.users.append(user)
            print("######----User Account Created---#####\n")
        else:
            self.admins.append(user)
            print("######----Admin Account Created---#####\n")

    def account_details(self, user):
        print("<----------Account Details-------->")
        print(f'Account Name : {user.name}')
        print(f'Account Type : {user.type}')
        print(f'{user.type} Phone Number : {user.phone}')
        print(f'{user.type} email : {user.email}')
        print(f'{user.type} address : {user.address}')
        print(f'{user.type} Balance : {user.balance}\n\n')

        




