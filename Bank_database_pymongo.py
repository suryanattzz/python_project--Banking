from pymongo import MongoClient

class bank_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["bank_database"]

    def insert_detail(self,x, y, z):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[x]
        db1 = db[x]
        db1.insert_one({"name": x, "Account no": y, "type": z})

    def display_detail(self, a, b, c):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[a]
        db1 = db[a]
        for i in db1.find({"name": a, "Account no": b, "type": c}).limit(1):
            print("Name of the account::", i["name"])
            print("Account Number::", i["Account no"])
            print("Type of the account::", i["type"])

    def insert_trans(self,a,b,c,r,s,t):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        coll_name = str(a)+str(b)+str(c)+str("trans")
        collection = db[coll_name]
        db1 = db[coll_name]
        db1.insert_one({"deposit":r, "withdraw":s, "balance":t})

    def display_trans(self,a,b,c):
        coll_name=str(a)+str(b)+str(c)+str("trans")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        print("Deposit   |", "Withdrawal   |", "Balance")
        for i in db2.find():
            print(i["deposit"], "\t\t\t", i["withdraw"], "\t\t\t", i["balance"])

    def insert_balance(self,a,b,c,d):
        coll_name = str(a)+str(b)+str(c)+str("bal")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        db2.insert_one({"name":a,"account no":b,"type":c,"current_balance":d})

    def drop_balance(self,a,b,c):
        coll_name = str(a)+str(b)+str(c)+str("bal")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        db2.drop()

    def get_balance(self,a,b,c):
        coll_name = str(a)+str(b)+str(c)+str("bal")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        for i in db2.find():
            return i["current_balance"]

    def insert_pin(self,a,b,c,d):
        coll_name = str(a) + str(b) +str(c)+str("pin")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        db2.insert_one({"name": a, "account no": b, "type": c, "pin":d})

    def drop_pin(self,a,b,c):
        coll_name = str(a)+str(b)+str(c)+str("pin")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        db2.drop()


    def get_pin(self,a,b,c):
        coll_name = str(a) + str(b) +str(c)+str("pin")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["bank_database"]
        collection = db[coll_name]
        db2 = db[coll_name]
        for i in db2.find():
            return i["pin"]


d = bank_database()