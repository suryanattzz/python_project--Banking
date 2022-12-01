from Bank_database_pymongo import *
import random
import sys


class bank():
    def __init__(self, balance=0.0, pin=1111):
        self.balance = balance
        self.pin = pin


    def get_info(self):
        self.name = input("Enter the account holder name :")
        self.accno = int(input("Enter the account no :"))
        self.type = input("Enter the type of account[Current / Savings]:")
        d.insert_detail(self.name, self.accno, self.type)
        d.insert_balance(self.name, self.accno,self.type,0)
        d.insert_pin(self.name,self.accno,self.type,self.pin)
        self.balance = d.get_balance(self.name,self.accno,self.type)
        self.pin = d.get_pin(self.name,self.accno,self.type)

    def display_info(self):
        print("\nWelcome To Banking System-->", self.name.upper())
        print(">>>Your Bank Account Has Been Created")
        print(">>>Your Four Digit Pin Is", self.pin)

    def display_option(self):
        print("\nSelect your next process from these options")
        print("""\t\t1 =>Account Details ,2 =>Deposit    ,3 =>Withdraw
        4 =>Current balance ,5 =>Change Pin ,6 =>Statement 
        7 =>Quit""")

    def pin_change(self, pin):
        if pin == self.pin:
            otp = random.randint(1000, 9999)
            print("Your OTP Is", otp)
            otp_input = int(input("Enter Your OTP: "))
            if otp == otp_input:
                print("Your OTP Has Been Verified")
                password_1 = int(input("\nEnter Your New Four Digit Pin: "))
                if 1000 <= password_1 > 999:
                    password_2 = int(input("Please Re-enter Your New Pin: "))
                    if password_1 == password_2:
                        self.pin = password_1
                        d.insert_pin(self.name,self.accno,self.type,self.pin)
                        print(">>>>You Have Sucessfully Changed Your Pin<<<<")
                        print(">>>Your Current Four Digit Pin Is", self.pin)
                    else:
                        print(">>>>You Re-entered your Pin Wrongly<<<<.\nPlease Try Again.")
                else:
                    print(">>>Enter Only Four Digit Pin")
            else:
                print(">>>Your OTP Is Incorrect.\nPlease Try Again")
        else:
            print("^^^^Enter correct four digit pin^^^^")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(">>>>You Have Deposited", amount, "Rupees", "In Your Account<<<<")
        print("Your Current Balance Is", self.balance, "Rupees")
        d.insert_trans(self.name,self.accno,self.type,amount,0,self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print(">>>>Withdraw Amount Exceeds Your Current Balance<<<<")
            print("Your Current Balance Is", self.balance, "Rupees")
        else:
            self.balance = self.balance - amount
            print(">>>>You have withdrawed", amount, "Rupees", "from your account<<<<")
            print("Your current balance after withdraw is", self.balance, "Rupees")
            d.insert_trans(self.name,self.accno,self.type,0,amount,self.balance)

    def current(self):
        print("****Your current balance is", self.balance, "Rupees****")

    def selection(self):
        select = int(input("\nEnter your next process: "))

        if select == 1:
            d.display_detail(self.name,self.accno,self.type)

        elif select == 2:
            password = int(input("Enter your four digit pin: "))
            if password == self.pin:
                otp = random.randint(1000, 9999)
                print("Your OTP Is", otp)
                otp_input = int(input("Enter Your OTP: "))
                if otp == otp_input:
                    print("Your OTP Has Been Verified")
                    amount = int(input("\nEnter the amount to be deposited: "))
                    o.deposit(amount)
                else:
                    print(">>>Your OTP Is Incorrect.\nPlease Try Again")
            else:
                print("^^^^Enter correct four digit pin^^^^")

        elif select == 3:
            password = int(input("Enter your four digit pin: "))
            if password == self.pin:
                otp = random.randint(1000, 9999)
                print("Your OTP Is", otp)
                otp_input = int(input("Enter Your OTP: "))
                if otp == otp_input:
                    print("Your OTP Has Been Verified")
                    amount = int(input("\nEnter the amount to be withdraw: "))
                    o.withdraw(amount)
                else:
                    print(">>>Your OTP Is Incorrect.\nPlease Try Again")
            else:
                print("^^^^Enter correct four digit pin^^^^")

        elif select == 4:
            password = int(input("Enter your four digit pin: "))
            if password == self.pin:
                o.current()
            else:
                print("^^^^Enter correct four digit pin^^^^")

        elif select == 5:
            password = int(input("Enter your four digit pin: "))
            if password == self.pin:
                o.pin_change(password)
            else:
                print("^^^^Enter correct four digit pin^^^^")

        elif select == 6:
            password = int(input("Enter your four digit pin: "))
            if password == self.pin:
                d.display_trans(self.name,self.accno,self.type)

            else:
                print("^^^^Enter correct four digit pin^^^^")

        elif select == 7:
            d.drop_balance(self.name,self.accno,self.type)
            d.insert_balance(self.name,self.accno,self.type,self.balance)
            d.drop_pin(self.name, self.accno, self.type)
            d.insert_pin(self.name, self.accno, self.type, self.pin)
            print("You have exited banking.\nThank You For Your Time")
            sys.exit("<-------->")

        else:
            print("You entered a invalid process")


print("\t\t\tWELCOME TO BANKING")

o = bank()
o.get_info()
o.display_info()

while (True):
    o.display_option()
    o.selection()