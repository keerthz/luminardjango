string=input("enter a string") #hello
ln=len(string)-1#4
res=""
i=0
while(ln>=0):#4>=0,
     res=res+string[ln]#0
     ln-=1

if(res==string):
    print("it is a palendrome")
else:
    print("not a palendrome")




