from re import*
f=open("gmaildetails","r")
list=[]
rule="\w*@gmail.com"
for line in f:
    data=line.rstrip("\n")
    list.append(data)
    matcher=fullmatch(rule,data)
    if(matcher !=None):
        print("valid gmail")
    else:
        print("invalid gmail")

