num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num2>num1) & (num1>num3)):
    print("num1 is largest",num1)
elif((num3>num2) & (num2>num1)):
    print("num2 is largest",num2)
elif((num1>num3) & (num3>num2)):
    print("num3 is largest",num3)
elif((num1==num2) & (num2==num3)):
    print("they are equall")
