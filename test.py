from Bank import Bank
from Admin import Admin
from User import User

def main():

    brac_bank = Bank("BRAC BANK")
    ab_bank = Bank("AB BANK")

    user_1 = User("Saiful")
    user_1.create_account(brac_bank, "saiful@yahoo.com", 1923452, "Dhaka")
    user_1.deposit(brac_bank, 50)
    brac_bank.account_details(user_1)

    admin_1 = Admin("Muktadir")
    admin_1.create_account(brac_bank, "muktadir@gmail.com", 1719324, "Rajshahi")
    admin_1.total_available_balance(brac_bank)
    admin_1.total_available_balance(ab_bank)
    admin_1.total_loan_amount(brac_bank)
    admin_1.total_loan_amount(ab_bank)

    user_1.transaction_history(brac_bank)
    


if __name__ == "__main__":
    main()