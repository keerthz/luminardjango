class bank:
    def __init__(self,accno,name,balance,bankname):
        self.accno=int(accno)
        self.name=name
        self.balance=int(balance)
        self.bankname=bankname
    def printvalues(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        print(self.bankname)

    def withdraw(self,amount):
        self.balance-=amount
        if(self.balance<amount):
            print("insufficient balance")
        else:
            print("remaining balance is",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("amount is credited",self.balance)
    def balanceenquiry(self):
        self.balance=amount
        print("account balance is",self.balance)
obj=bank(1452222,"arun","25000","bankname")
obj.printvalues()

