class employee:

    def __init__(self,eid,ename,desig):
        self.id=eid
        self.name=ename
        self.desig=desig

    def printvalues(self):
        print("eid=",self.id)
        print("ename=",self.name)
        print("desig=",self.desig)
obj=employee(1001,"rahul","ceo")
obj.printvalues()