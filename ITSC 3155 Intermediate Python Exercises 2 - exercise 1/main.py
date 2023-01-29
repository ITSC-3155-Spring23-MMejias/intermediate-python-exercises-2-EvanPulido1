# Evan Pulido
# ITSC 3155

# The link that helped me import classes: https://www.geeksforgeeks.org/how-to-import-a-class-from-another-file-in-python/
import BankAccount

# Create a class object
object = BankAccount.BankAccount()

# Hard coded account name and starting balance
account_name = 'MysteryMan' 
starting_balance = 5 # 5 dollars

# Ask the user to deposit any amount of money into account
deposit_money = float(input('Enter how much money you would like to deposit: '))
balance = object.deposit(deposit_money, starting_balance)

# Ask the user to withdraw any amount of money into account
withdraw_money = float(input('Enter how much money you would like to withdraw: '))
balance = object.withdraw(withdraw_money, balance)

# Print the get_balance method
print(object.get_balance(account_name, balance))