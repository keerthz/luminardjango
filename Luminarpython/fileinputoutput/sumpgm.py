#f=open("numbers","r")
#lst=[]
#for numbers in f:
#    numbers=int(numbers.rstrip("\n"))
#    lst.append(numbers)
#print(sum(lst))

#for numbers in f:
#   number=numbers.rstrip("\n")
#    lst.append(number)
#print(lst)
f=open("numbers","r")
lst=[]
for numbers in f:
    number=int(numbers.rstrip("\n"))
    lst.append(number)
print(sum(lst))