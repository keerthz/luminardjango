string=input("enter a word")
list=["a","e","i","o","u"]
count=0

for i in list:
    if(i in string):
        count+=1
        print(count,i)
    else:

        break

