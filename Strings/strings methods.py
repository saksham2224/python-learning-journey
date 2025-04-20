# strings are immutable

name = "hello world"

# name[0] = "S" #we cannot do this it will crete an error 

a = len(name) #len function finds the length or size of string
print(a)

b = name.capitalize() #Capatalize function helps to make fist character of string capital
print(b)

c = name.upper()#all caracter of string in upper case
d = name.lower()#all character of string in lower case
e = name.title()#first character of each word in uper case

print(c,d,e,sep="\n")

# Removing Whitespace
text = " hello world "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"


name = "Saksham Jain"
print(name.find("Jain")) 
print(name.replace("Jain","Chandariya"))

fruits = "apples,bananas,grapes,pineapples"

split= fruits.split(",")
print(split)
print(type(split))
   
join = ",".join(split)
print(join)
print(type(join))



password = "saksham23"

print(password.isalpha())
print(password.isalnum())
print(password.isdigit())
print(password.isspace())



# FOR HANDLE ASCII VALUES 

print(ord("A"))
print(chr(65))


