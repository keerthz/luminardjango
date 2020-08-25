class employee:
    def setemployee(self,eid,ename,edesig):
        self.eid=eid
        self.ename=ename
        self.edesig=edesig
    def printvalues(self):
        print(self.eid)
        print(self.ename)
        print(self.edesig)
obj=employee()
obj.setemployee(1001,"rahul","ceo")
obj.printvalues()



