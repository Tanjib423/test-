print('Hello world')
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)
print("the factorial of 11 is",factorial(11))