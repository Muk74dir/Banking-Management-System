from Bank import Bank
from Admin import Admin
from User import User


user_1 = User("Muktadir", "muktadir@gmail.com", "dhaka", 23923)

user_1.create_account()

print(user_1.balance)
user_1.deposit(20)
print(user_1.balance)

user_2 = User("Saiful", "saiful@gmail.com", "rajshahi", 2323)

user_1.transfer_balance(user_2, 20)
print(user_2.balance)
print(user_1.balance)

