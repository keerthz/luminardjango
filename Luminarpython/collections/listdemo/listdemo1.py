#lst=[100,200,300,400,500,600]
#sum=0
#for item in lst:
#    sum+=item
#print(sum)
#lst=[]
#even=[]
#odd=[]
#for i in range(0,501):
#lst.append(i)
#if(i%2==0):
#even.append(i)
#else:
#odd.append(i)
#print(even)
#print(odd)

#lst=[3,5,8]
#output=[]
#total=sum(lst)
#for item in lst:
#    num=total-item
#    output.append(num)
#print(output)

lst=[10,20,30,44,12248,1222]
element=int(input("enter the number for search"))
flag=0
for i in lst:
    if(i==element):
        flag=1
        break

    else:
        flag=0
if(flag==1):
    print("element found")
else:
    print("not found")









