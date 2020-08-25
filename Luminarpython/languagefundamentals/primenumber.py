number=int(input("enter the number for checking prime"))
flg=0
for i in range(2,7):#7%2==0,7%3==0
    if(number%i==0):
        flg=1
        break
if(flg==0):
     print("prime")
else:
    print("not prime")






#2,3,4,5,6
