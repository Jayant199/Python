he
# Datatypes

# To find the datatype

a=5.0


print("Data type is ", type(a))

#Numeric

# To get the complex form of the input provided 
a=int(input("Enter the real part"))
b=int(input("Enter the imaginary part"))
c=complex (a,b)
print("The complex representation is", (c))

#strings

#To search the postion of the word

a=str(input("Enter the word"))
i=int(input("Enter the position to be searched in the word"))

print(a[i])

#To print the string the number of times you want

a=str(input("Enter the word"))
i=int(input("Enter the number of times you want to get it printed"))

print(a*i)

#List

#To display the character on the particular position in a list

print("Enter numbers to create your list")


a=int(input("Enter your Number"))
b=int(input("Enter your Number"))
c=int(input("Enter your Number"))
d=int(input("Enter your Number"))
e=int(input("Enter your Number"))

l=[a,b,c,d,e]

print("Your list is ",l)

i=int(input("Enter the postion to search in the list"))

print (l[i])


#To add 2 Strings

print("Enter numbers to create your first list")


a=int(input("Enter your Number"))
b=int(input("Enter your Number"))
c=int(input("Enter your Number"))
d=int(input("Enter your Number"))
e=int(input("Enter your Number"))

l=[a,b,c,d,e]

print("Your first list is ",l)

print("Enter numbers to create your second list")


f=int(input("Enter your Number"))
g=int(input("Enter your Number"))
h=int(input("Enter your Number"))
i=int(input("Enter your Number"))
j=int(input("Enter your Number"))

k=[f,g,h,i,j]

print("Your first list is ",k)
      
print(l+k)


# Dictionary

d={1:200,2:300,3:400,4:500,5:600}

i=int(input("Enter a key value to search"))

print(d[i])


#To print all key values


d={1:200,2:300,3:400,4:500,5:600}


print("All the key values are",d.keys())

#To print all value values in a dictionary

      

d={1:200,2:300,3:400,4:500,5:600}


print("All the value values are",d.values())



      

