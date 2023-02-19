# Evan Pulido
# ITSC 3155-151

# Link that taught me about classes and objects: https://www.w3schools.com/python/python_classes.asp
# A bank account class
class BankAccount:
    # Constructor that takes in account name and starting balance and stores them as instance fields
    def __init__(self, a_n = '', s_b = 0):
        self.account_name = a_n
        self.starting_balance = s_b

    # Link that helps me write methods: https://www.w3schools.com/python/python_functions.asp
    # Method that deposits some amount of money into the account
    def deposit(self, d_m, s_b):
        balance = 0
        balance += d_m
        return s_b + balance

    # Method that withdraws some amount of money from the account
    def withdraw(self, w_m, b):
        b -= w_m
        return b

    # Method that returns a string that says {account name} has a balance of "balance"
    def get_balance(self, a_n, s_b):
        return a_n + ' has a balance of $' + str(s_b)
