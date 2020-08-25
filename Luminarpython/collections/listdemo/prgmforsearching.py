lst=[10,12,13,14,15]
element=int(input("enter the element for search"))
flg=0
for i in lst:
    if(i==element):

        flg=1
        break
    else:
        flg=0
if(flg==1):
    print("element found")
else:
    print("not found")