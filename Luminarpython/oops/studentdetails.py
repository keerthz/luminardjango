class student:
    def __init__(self,name,rollno,grade):
        self.name=name
        self.rollno=int(rollno)
        self.grade=grade
    def printvalues(self):
        print(self.name)
        print(self.rollno)
        print(self.grade)
obj=student("keerthana",23,"A")

obj.printvalues()
