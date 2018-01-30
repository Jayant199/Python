
# Nested if

# To evaluate the grade of a student
n=int(input("Enter you total marks"))
if (n<=100):
    if(n<0 and n<=63):
        print ("Grade : F")

    if (n>63 and n<=75):
        print ("Grade : C")
        
    if (n>75 and n<=95):
        print ("Grade : B")

    if (n>95 and n<=100):
        print ("Grade : A")

else:
    print("Invalid marks")
               
               
               
               
