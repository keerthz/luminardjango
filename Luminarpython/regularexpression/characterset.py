from re import*
#pattern='[a-zA-Z]' for print lower case letters from a-z and upper case letter from A-Z
#pattern="[^a-zA-Z0-9]" for print special character
#pattern="\s" for space
#pattern="\d" for print
#pattern="\D"
#pattern="\w"
#pattern="\W"
#count=0
matcher=finditer(pattern,"abx 7@dfgg#%&")
for match in matcher:
    print(match.start())
    print(match.group())