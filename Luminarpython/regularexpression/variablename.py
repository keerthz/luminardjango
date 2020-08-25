from re import*
rule="[a-k][369][a-z]*"

varname=input("enter a validname")

matcher=fullmatch(rule,varname)

if(matcher !=None):
    print("valid")
else:
    print("invalid")
