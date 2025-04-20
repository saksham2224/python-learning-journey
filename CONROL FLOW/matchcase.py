operator = input("Enter Any Of These Operator(\"+,-,*,/\") ")
# print(type(operator))
a = int(input("Enter A Numbers : "))
b = int(input("Enter Second  Numbers : "))
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "/":
        print(a/b)
    case "*":
        print(a*b)
    case _:   
        print("Something Wemt Wwong")    


