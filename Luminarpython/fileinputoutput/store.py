#f=open("numbers","r")
#lst=[]
#for numbers in f:
#    number=numbers.rstrip("\n")
#    lst.append(number)
#print(lst)
f=open("numbers","r")
lst=[]
for numbers in f:
    number=numbers.rstrip("\n")
    lst.append(number)
print(lst)