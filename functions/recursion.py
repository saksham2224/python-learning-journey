#A function calling itselg to solve any problem is known as recursion

def fibonachi(n):
    if n == 0 or n == 1:
        return n
    return fibonachi(n-2)+fibonachi(n-1)

print(fibonachi(7))





