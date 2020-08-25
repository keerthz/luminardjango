import datetime

class person:
    def setValues(self,pname,age):
        self.pname=pname
        self.age=age
    def printValues(self):
        print(self.pname)
        print(self.age)

class bank(person):
    bankname="SBI"
    def __init__(self,accnum):
        self.accnum=accnum
        self.balance=10000

    def withraw(self,amount):
        self.balance-=amount
        if(self.balance<amount):
            print("the transaction has been cancelled errorcode 10012")

        else:
            print("your", bank.bankname, "has been debited of ", amount, "on", datetime.date.today())

    def deposit(self,amount):
        self.balance+=amount
        print("your",bank.bankname,"has beed credited with",amount,"on",datetime.date.today() )
    def balanceEnquiry(self):

        print("the account balance is",self.balance)
obj=bank(1011546)
obj.setValues("arun",25)
obj.printValues()
obj.withraw(5000)
obj.balanceEnquiry()

