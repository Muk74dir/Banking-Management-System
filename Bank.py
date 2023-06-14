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

    def create_account(self, user, initail_deposit):
        user = user
        self.users.append(user)

        




