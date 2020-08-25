num1=int(input("enter the value for num1"))
num2=int(input("enter the value for num2"))
pos=int(input("enter the pos"))
lst=[1,2,3,4]
try:
    res=num1/num2

    print("result=",res)
except Exception as e:
    print(e.args)
try:
    print(lst[pos])

except Exception as e:
    print(e.args)
finally:

    print("we have database transactions")
    print("file operation")
    print("process completed sucessfully")