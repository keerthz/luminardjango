lst=[3,5,8]#output[13,11,8]
#3+5+8=16
#16-3=13
#16-5=11
#16-8=8
output=[]
total=sum(lst)
for item in lst:
    num=total-item#16-3=13
    output.append(num)
print(output)
