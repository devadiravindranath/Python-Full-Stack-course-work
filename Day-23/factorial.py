def factorial(n,fact):
    if n == 0:
        return fact
    return factorial (n-1,fact*n)

print(factorial(8,1))