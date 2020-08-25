class employee:

    def __init__(self,eid,ename,desig):
        self.id=eid
        self.name=ename
        self.desig=desig

    def printvalues(self):
        print("eid=",self.id)
        print("ename=",self.name)
        print("desig=",self.desig)

    def __str__(self):
        return self.name

obj=employee(10001,"ajay","ceo")
print(obj)