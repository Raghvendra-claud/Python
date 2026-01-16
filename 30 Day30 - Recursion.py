def factorial(num):
    if( num == 1 or num == 0 ):
        return 1
    else:
        return num * factorial(num - 1)
    
def fib(num):
    if( num == 0 ):
        return 0
    elif( num == 1 ):
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

num = int(input("enter number: "))
# print(f"factorial of {num} is",factorial(num))
print(f"fibonaaci still num is {num} is",fib(num))