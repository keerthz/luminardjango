num1=int(input("enter the value for num1"))
num2=int(input("enter the value for num2"))
lst=[1,2,3,4]
try:
    res=num1/num2

    print("result=",res)
    pos = int(input("enter index position"))
    print(lst[pos])
    print("we have database transactions")
    print("file operation")
    print("process completed sucessfully")

except exception as e:
    print(e.args)
