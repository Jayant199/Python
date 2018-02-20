#defining functions
a=int(input("Enter x"))
b=int(input("Enter y"))

def add(x,y):
    return x+y
print("")
print("Addition of",a,"and",b,"is" ,(add(a,b)))

a=int(input("Enter x"))
b=int(input("Enter y"))

def sub(x,y):
    return x-y
print("")
print("Subtraction of",a,"and",b,"is" ,(sub(a,b)))

a=int(input("Enter x"))
b=int(input("Enter y"))

def mul(x,y):

    return x*y
print("")  
print("Multiplication of",a,"and",b,"is" ,(mul(a,b)))

a=int(input("Enter x"))
b=int(input("Enter y"))

def mod(x,y):
   
    return x%y
print("")   
print("Modulus of",a,"and",b,"is" ,(mod(a,b)))


a=int(input("Enter x"))
b=int(input("Enter y"))

def powe(x,y):

    return x**y
print("") 
print("Power of",a,"to",b,"is" ,(powe(a,b)))


a=int(input("Enter x"))
b=int(input("Enter y"))

def div(x,y):

    return x/y
print("")
print("Division of",a,"by",b,"is" ,(div(a,b)))

a=int(input("Enter x"))
b=int(input("Enter y"))

def flo(x,y):

    return x//y
print("")
print("Float division of",a,"and",b,"is" ,(flo(a,b)))



