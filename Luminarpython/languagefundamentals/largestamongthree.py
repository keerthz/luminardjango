num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2) & (num1>num3)): #30>10 ,30>20
    print("num1 is largest",num1)#30
elif((num2>num1) & (num2>num3)): #40>20 ,40>30
    print("num2 is largest", num2) #40
elif((num3>num1) & (num3>num2)):# 50>10,50>20
    print("num3 is largest", num3) #50
elif((num1==num2) & (num2==num3)):
    print("they are equall")