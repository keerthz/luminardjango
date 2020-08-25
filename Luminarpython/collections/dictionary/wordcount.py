#list="hai good morning have a good day"
#words=list.split(" ")
#dict={}
#for word in words:
#   if(word not in dict):
#       dict[word]=1
#   else:
#       dict[word]+=1
#print(dict)

list="hai good morning have a good day hai good"
words=list.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)