from functools import*
class employee:
    def __init__(self,id,name,desig,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=int(sal)

    def printValues(self):
        print("name=",self.id)
        print(self.name)
        print(self.desig)
        print("salary=",self.sal)
    def __str__(self):

        return self.name

f=open("employee","r")
emplist=[]
for data in f:
    values = data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=employee(id, name, desig, salary)
    emplist.append(obj)
upperName=list(map(lambda employee:employee.name.upper(),emplist))
salaryadd=list(map(lambda employee:employee.sal+5000,emplist))
maxsal=list(filter(lambda employee:employee.sal>25000,emplist))
print(upperName)
print(salaryadd)
for emp in maxsal:
    print(emp)



