
def table():
    print("This Program Helps User To Print A Table Of any Number Given By The User")

    a = int(input("\nEnter A Number: "))

    for i in range(1,11):
         print(f"{a}*{i} = ", a*i)

table()