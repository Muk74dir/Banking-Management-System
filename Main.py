from Bank import Bank
from Admin import Admin
from User import User

def main():
    print("Main is running\n")

    brac_bank = Bank()
    admin_1 = Admin("Muktadir", "muktadir@hotmail.com", "Rajshahi", 583274)
    brac_bank.create_account(admin_1)
    brac_bank.account_details(admin_1)

    user_1 = User("Saiful", "saiful@xyz.com", "Dhaka", 9238)
    brac_bank.create_account(user_1)
    brac_bank.account_details(user_1)

    user_2 = User("Rajoni", "rajoni@yahoo.com", "Rangpur", 23245)
    brac_bank.create_account(user_2)
    brac_bank.account_details(user_2)



    






if __name__ == "__main__":
    main()