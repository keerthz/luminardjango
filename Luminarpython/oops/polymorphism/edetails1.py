class employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    def printEmp(self):
        print("name=",self.name)
        print("desig=",self.desig)

    def __str__(self):

        return self.name

f=open("edetails","r")
emplst=[]
for data in f:
    "100,suraj,centerhead,30000"

    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=employee(id,name,desig,salary)
    emplst.append(obj)

for emp in emplst:
    print(emp)
