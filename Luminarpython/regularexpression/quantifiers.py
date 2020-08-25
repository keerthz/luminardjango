import re
#pattern="a+"
#pattern="a*"
#pattern="a?"
#pattern="a{2}"
pattern="a{2,3}"
matcher=re.finditer(pattern,"aabaaaabbaaaaaabaaabb")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("count",count)