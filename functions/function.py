def averageofthree(a,b,c):
    average = (a+b+c)//3
    return average

# result = averageofthree(10,20,30)
# print(result)

def add(a,b):# positional argument
    x = a+b
    return x
#a and b are parameters and and 3 and  5 are arguments
c = add(3,5)
print(c)

def add1(a,b,plus = 0):#plus is a default parameter it not necessary to pass any argument for it if we paas argument the value of plus is overwrite: 
    x1 = a + b+ c
    return(x1)

resulr=add1(2,3,6)
print(resulr)
 
def Fullname(surname , name):
    return f"Your Name Is {name} {surname}"

loo = Fullname(name = "Saksham",surname = "jain")#this is known as keyword arguments
print(loo)

