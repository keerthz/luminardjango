from re import*
#rule="[a-z][a-z0-9]*[@][g][m][a][i][l][.][c][o][m]"#"\w*[@]gmail.com"
rule="\w*[@]gmail.com"
gmail=input("enter gmail")
matcher=fullmatch(rule,gmail)
if(matcher !=None):
    print("valid")
else:
    print("invalid")