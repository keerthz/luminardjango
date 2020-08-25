
lst=[1,2,3,4]
element=6
low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(element==data):
        print(lst[low],",",lst[upp])
        break

    else:
        low=low+1




