
import random
computer=random.choice([0,1])
youstr=input("Enter Your choice: ")
youDict={"Head":0,"Tail":1}
reversedict={0:"Head",1:"Tail"}
you=youDict[youstr]
print(f"you choose: {reversedict[you]}\ncomputer choose: {reversedict[computer]}")
if(computer==you):
    print("Its Draw")
else:
    if(computer==0 and you==1):
        print("You win")
    elif(computer==1 and you==0):
        print("you lose")
    else:
        print("something went wrong")