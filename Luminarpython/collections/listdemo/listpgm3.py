lst=[]
even=[]
odd=[]
for i in range(0,501):
    lst.append(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)