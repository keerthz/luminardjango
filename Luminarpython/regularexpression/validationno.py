from re import*
rule="\d{10}"
mobileno=input("enter mobilenumber")
matcher=fullmatch(rule,mobileno)
if(matcher !=None):
    print("valid")
else:
    print("invalid")