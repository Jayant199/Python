#ROCKPAPERSCISSORS
import random 
L=["Rock","Paper","Scissors"]
count=0
while(count<=5):
    computer=random.choice(L)
    user=input("Enter Rock, Paper or Scissor")
    count+=1
    if (user=="Rock"):
        if(computer==user):
            print ("Clash")
            
        elif(computer=="Paper"):
            print("Paper shadowed the rock, Computer wins")
            
        else:
            print("Scissors were crushed by the stone, You win")

        
    elif (user=="Paper"):
        if(computer==user):
            print ("Clash")
            
        elif(computer=="Rock"):
            print("Paper shadowed the rock, You win")
            
        else:
            print("Scissors cut the paper, You lose")

        
    elif (user=="Scissor"):
        if(computer==user):
            print ("Clash")
            
        elif(computer=="Paper"):
            print("Scissors cut the paper, You win")
            
        else:
            print("Rock crushed the Scissors, You lose")

            
