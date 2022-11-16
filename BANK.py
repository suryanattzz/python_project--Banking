                #BANKING SYSTEM

import sys

class bank():
    def __init__(self,name,balance=0.0):
        self.name=name,
        self.balance=balance

    def display(self):
        print("\n", name, "welcome to banking system")
        print("\nYour bank account has been created")
        print("\nselect your next process from these options")
        print("1.deposit,2.withdraw,3.current balance,4.quit")


    def deposit(self,amount):
        self.balance=self.balance+amount
        print("You have deposited",amount,"in your account")
        print("your current balance is", self.balance)

    def withdraw(self,amount):
        if self.balance<amount:
            print("Withdraw amount exceeds your current blance")
            print("your current balance is", self.balance)
        else:
            self.balance=self.balance-amount
            print("you have withdrawed",amount,"from your account")
            print("your current balance after withdraw is",self.balance)

    def current(self):
        print("your current balance is", self.balance)

    def selection(self):
        select = int(input("\nenter your next process: "))

        if select == 1:
            amount = int(input("\nEnter the amount to be deposited: "))
            o.deposit(amount)

        elif select == 2:
            amount = int(input("\nEnter the amount to be withdraw: "))
            o.withdraw(amount)

        elif select == 3:
            o.current()

        else:
            print("you entered a invalid process")
            quit()

name=input("\nenter your name to create the account: ")
o=bank(name)
print(o.display())

while(True):
    o.selection()




























