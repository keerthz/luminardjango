import functools
class employee:

    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=int(salary)

    def printEmp(self):
        print(self.id)
        print("name=",self.name)
        print(self.desig)
        print("salary",self.salary)

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

upperename=list(map(lambda employee:employee.name.upper(),emplst))
salarylist=list(map(lambda employee:employee.salary+5000,emplst))
maxsalary=list(filter(lambda employee:employee.salary>25000,emplst))

print(upperename)
print(salarylist)
for emp in maxsalary:
    print(emp)

salary=list(map(lambda obj:obj.salary,emplst))
print(salary)
maxsalary=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print(maxsalary)




