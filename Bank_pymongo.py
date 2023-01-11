from Bank_database_pymongo import *
import re
import random
import sys


class bank():
    def __init__(self, balance=0.0, pin=1111,count=0):
        self.balance = balance
        self.pin = pin
        self.count = count

    def login_option(self):
        print("To Proceed Further Choose The Below Options.")
        print("\n 1=> Create New Account")
        print("\n 2=> Login into Exiting Account.")
        print("\n 3=> Forget Pin.")
        print("\n 4=> Recover Account.")
        print("\n 5=> Quit.")
        self.option = int(input("Enter Your Option::"))
        o.login_sel()

    def login_sel(self):
        if self.option == 1:
            self.name = input("Enter the account holder name :")
            self.type = input("Enter the type of account[Current / Savings]:")
            self.aadhaar = int(input("Enter Your Aaadhaar: "))
            if bool(re.match(r"^\d{12}$", str(self.aadhaar))) == True and \
                    bool(re.match(r"^[a-zA-Z ]+$", self.name)) == True:
                if d.ser_login_acc(self.name,self.aadhaar,self.type)!=1:
                    print("\nYour Account Should Have Minimum Balance Of 500 Rupees.")
                    amount = abs(int(input("\nEnter the amount to be deposited: ")))
                    if amount>=500:
                        self.accno = random.randint(10000000000, 99999999999)
                        o.deposit(amount)
                        print("Your Account Number Is", self.accno)
                        d.insert_detail(self.name, self.accno, self.type, self.aadhaar)
                        d.insert_balance(self.name, self.accno, self.type,self.balance)
                        d.insert_pin(self.name, self.accno, self.type, self.pin)
                        print("\nWelcome To Banking System-->", self.name.upper())
                        print(">>>Your Bank Account Has Been Created")
                        print(">>>Your Four Digit Pin Is", self.pin)
                    else:
                        print("You Have Deposited Less Than 500 Rupees .")
                        print("Please Try Again.")
                        o.login_option()
                else:
                    print("There is Another Account with your Aadhaar Number.")
                    o.login_option()
            else:
                print("Please Enter Valid Input To Create Account.")
                o.login_option()

        elif self.option == 2:
            self.name = input("Enter the account holder name :")
            self.accno = int(input("Enter the account no :"))
            self.type = input("Enter the type of account[Current / Savings]:")
            if d.acc_search(self.name, self.accno, self.type) == 1:
                while self.count < 3:
                    password = int(input("Enter your four digit pin: "))
                    self.pin = d.get_pin(self.name, self.accno, self.type)
                    if password == self.pin :
                        self.balance = d.get_balance(self.name, self.accno, self.type)
                        print("\nWelcome To Banking System-->", self.name.upper())
                        self.count = 0
                        break
                    else:
                        print("^^^^Enter correct four digit pin^^^^")
                        self.count = self.count + 1
                        print("No Of Tries Left=>>",3-self.count)
                        if self.count == 3:
                            print("You Have Exceeded No of Tries.")
                            self.count = self.count * 0
                            o.login_option()

            else:
                print("\nYour account is not registered in our database")
                print("Please enter valid input OR Create New Account.")
                o.login_option()

        elif self.option == 3:
            o.forget_pin()
            o.login_option()

        elif self.option == 4:
            self.name = input("Enter the account holder name :")
            self.aadhaar = int(input("Enter Your Aaadhaar: "))
            result = d.ser_rec_acc(self.name, self.aadhaar)
            if result == 1:
                print("\n")
                d.disp_rec_acc(self.name, self.aadhaar)
                self.pin = 1111
                d.drop_pin(self.name, self.accno, self.type)
                d.insert_pin(self.name, self.accno, self.type, self.pin)
                print(">>>Your Current Four Digit Pin Is", self.pin)
                o.login_option()
            else:
                print("Please Provide Valid Details To Fetch Data.")
                o.login_option()

        elif self.option == 5:
            print("You have exited banking.\nThank You For Your Time")
            sys.exit("<-------->")

        else:
            print("You entered a invalid process")
            o.login_option()

    def forget_pin(self):
        self.name = input("Enter the account holder name :")
        self.accno = int(input("Enter Your Account Number:"))
        self.type = input("Enter the type of account[Current / Savings]:")
        self.aadhaar = int(input("Enter Your Aaadhaar: "))
        if d.ser_acc_pin(self.name, self.accno, self.aadhaar) == 1:
            password_1 = int(input("\nEnter Your New Four Digit Pin: "))
            if 1000 <= password_1 > 999:
                password_2 = int(input("Please Re-enter Your New Pin: "))
                if password_1 == password_2:
                    self.pin = password_1
                    d.drop_pin(self.name, self.accno, self.type)
                    d.insert_pin(self.name, self.accno, self.type, self.pin)
                    print(">>>>You Have Sucessfully Changed Your Pin<<<<")
                    print(">>>Your Current Four Digit Pin Is", self.pin)
                else:
                    print(">>>>You Re-entered your Pin Wrongly<<<<.\nPlease Try Again.")
            else:
                print(">>>Enter Only Four Digit Pin")
        else:
            print("Please Enter Valid Input.")

    def display_option(self):
        print("\nSelect your next process from these options")
        print("""\t1 =>Account Details ,2 =>Deposit    ,3 =>Withdraw
        4 =>Current balance ,5 =>Change Pin ,6 =>Statement 
        7 =>Quit""")
        o.selection()

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
                        d.insert_pin(self.name, self.accno, self.type, self.pin)
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
        d.insert_trans(self.name, self.accno, self.type, amount, 0, self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print(">>>>Withdraw Amount Exceeds Your Current Balance<<<<")
            print("Your Current Balance Is", self.balance, "Rupees")
        else:
            self.balance = self.balance - amount
            print(">>>>You have withdrawed", amount, "Rupees", "from your account<<<<")
            print("Your current balance after withdraw is", self.balance, "Rupees")
            d.insert_trans(self.name, self.accno, self.type, 0, amount, self.balance)

    def current(self):
        print("****Your current balance is", self.balance, "Rupees****")

    def selection(self):
        self.select = int(input("\nEnter your next process: "))

        if self.select == 1:
            d.display_detail(self.name, self.accno, self.type)

        elif self.select == 2:
            while self.count<3:
                password = int(input("Enter your four digit pin: "))
                if password == self.pin:
                    otp = random.randint(1000, 9999)
                    print("Your OTP Is", otp)
                    otp_input = int(input("Enter Your OTP: "))
                    if otp == otp_input:
                        print("Your OTP Has Been Verified")
                        amount = abs(int(input("\nEnter the amount to be deposited: ")))
                        o.deposit(amount)
                        self.count=0
                        break
                    else:
                        print(">>>Your OTP Is Incorrect.\nPlease Try Again")
                else:
                    print("^^^^Enter correct four digit pin^^^^")
                    self.count = self.count + 1
                    print("No Of Tries Left=>>", 3 - self.count)
                    if self.count == 3:
                        print("You Have Exceeded No Of Tries.")
                        self.count = self.count * 0
                        o.login_option()

        elif self.select == 3:
            while self.count < 3:
                password = int(input("Enter your four digit pin: "))
                if password == self.pin:
                    otp = random.randint(1000, 9999)
                    print("Your OTP Is", otp)
                    otp_input = int(input("Enter Your OTP: "))
                    if otp == otp_input:
                        print("Your OTP Has Been Verified")
                        amount = abs(int(input("\nEnter the amount to be withdraw: ")))
                        o.withdraw(amount)
                        self.count = 0
                        break
                    else:
                        print(">>>Your OTP Is Incorrect.\nPlease Try Again")
                else:
                    print("^^^^Enter correct four digit pin^^^^")
                    self.count = self.count + 1
                    print("No Of Tries Left=>>", 3 - self.count)
                    if self.count == 3:
                        print("You Have Exceeded No of Tries.")
                        self.count = self.count * 0
                        o.login_option()

        elif self.select == 4:
            while self.count<3:
                password = int(input("Enter your four digit pin: "))
                if password == self.pin:
                    o.current()
                    self.count = 0
                    break
                else:
                    print("^^^^Enter correct four digit pin^^^^")
                    self.count=self.count+1
                    print("No Of Tries Left=>>", 3 - self.count)
                    if self.count==3:
                        print("You Have Exceeded No of Tries.")
                        self.count=self.count*0
                        o.login_option()

        elif self.select == 5:
            while self.count < 3:
                password = int(input("Enter your four digit pin: "))
                if password == self.pin:
                    o.pin_change(password)
                    self.count = 0
                    break
                else:
                    print("^^^^Enter correct four digit pin^^^^")
                    self.count = self.count + 1
                    print("No Of Tries Left=>>", 3 - self.count)
                    if self.count == 3:
                        print("You Have Exceeded No of Tries.")
                        o.login_option()
                        self.count = self.count * 0

        elif self.select == 6:
            while self.count < 3:
                password = int(input("Enter your four digit pin: "))
                if password == self.pin:
                    d.display_trans(self.name, self.accno, self.type)
                    self.count = 0
                    break
                else:
                    print("^^^^Enter correct four digit pin^^^^")
                    self.count = self.count + 1
                    print("No Of Tries Left=>>", 3 - self.count)
                    if self.count == 3:
                        print("You Have Exceeded No of Tries.")
                        self.count = self.count * 0
                        o.login_option()

        elif self.select == 7:
            d.drop_balance(self.name, self.accno, self.type)
            d.insert_balance(self.name, self.accno, self.type, self.balance)
            d.drop_pin(self.name, self.accno, self.type)
            d.insert_pin(self.name, self.accno, self.type, self.pin)

        else:
            print("You entered a invalid process")


print("\t\t\tWELCOME TO BANKING")

o = bank()

while True:
    o.login_option()
    o.display_option()
    while o.select != 7:
        o.display_option()
