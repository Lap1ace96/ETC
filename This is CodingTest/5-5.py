def factorial_iteractive(n):
    result = 1
    for i in range (1,n+1):
        result = result * i
    return result

def factorial_recursive(n):
    if n==1:
        return 1   
    return n * factorial_recursive(n-1)

print(factorial_iteractive(5))
print(factorial_recursive(5))