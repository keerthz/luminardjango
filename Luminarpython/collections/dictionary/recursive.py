#pat="BABACCDEFAHBSND"
#lst=[]
#dict={}
#for letters in pat:
#    lst.append(letters)
#print(lst)
#for word in lst:
#        if(word not in dict):
#            dict[word]=1
#        else:
#            print("first recursive word",word)
#            break
pat="ASDCDDEFFGTUU"
lst=[]
dict={}
for letters in pat:
    lst.append(letters)
print(lst)
for word in lst:
    if(word not in dict):
        dict[word]=1
    else:
        print("first recursive word",word)
        break