class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=int(salary)

    #def printValues(self):
     #   print(self.id)
      #  print(self.name)
       # print(self.salary)

obj=employee(1001,"ayay",25000)
obj2=employee(1002,"arun",30000)
obj3=employee(1003,"jinu",35000)

lst=[]
lst.append(obj)
lst.append(obj2)
lst.append(obj3)

for employee in lst:
    if(employee.salary>=35000):
        print(employee.name)








