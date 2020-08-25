mk1=int(input("enter mk1"))
mk2=int(input("enter mk2"))
mk3=int(input("enter mk3"))
total=(mk1+mk2+mk3)
print(total)
if(total>145):
    print("grade A+")
elif((total>140) & (total<=145)):
    print("grade A")
elif((total>135) & (total<=140)):
    print("grade B+")
elif((total>130) & (total<=135)):
    print("grade B")
elif((total<130)):
    print("fail")





