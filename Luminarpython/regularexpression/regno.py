from re import *
f=open("reg","r")
list=[]
rule='[kK][lL][0-9]{2}[a-z]{2}\d{4}'

for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher !=None):
        print("valid")
        list.append(data)

    else:
        print("invalid")
