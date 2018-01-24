# Sanke and ladder

import random

count=0

while int(count<=100):
    i=input("Press r to roll a dice")
    if i=="r":
        a=random.randint(1,6)
        count=count+a
        print(a,count)
    if count==8:
        count=37
        print("Its a ladder, come up")
        count=count+a
    elif count==52:
        count=81
        print("Its a ladder, come up")
        count=count+a
    elif count==40:
        count=68
        print("Its a ladder, come up")
        count=count+a
    elif count==76:
        count=97
        print("Its a ladder, come up")
        count=count+a
    elif count==11:
        count=2
        print("Snake bite, come down")
        count=count+a
    elif count==25:
        count=4
        print("Snake bite, come down")
        count=count+a
    elif count==65:
        count=46
        print("Snake bite, come down")
        count=count+a
    elif count==89:
        count=70
        print("Snake bite, come down")
        count=count+a
    elif count==38:
        count=9
        print("Snake bite, come down")
        count=count+a
    elif count==93:
        count=64
        print("Snake bite, come down")
        count=count+a
    elif count==100:
        print("You Win!")

        

        
    
        
