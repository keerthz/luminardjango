#lst=[1,2,3,4]
#element=6
#low=0
#upp=len(lst)-1

#for i in lst:
#    data=lst[low]+lst[upp]
#    if(element==data):
#        print(lst[upp],",",lst[low])

 #       break
 #   else:
 #       low+=1

pat="ASDFDDDFFSERFFDGHHJJKLOOOCVCXMCMMJ"
lst=[]
dict={}
for letters in pat:
    lst.append(letters)
print(lst)
for word in lst:
    if(word not in dict):
        dict[word]=1

    else:
        print("first recursive word found",word)
        break


