def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print("6!:", factorial(6))

def factorial_1(n):
    if n == 0:
        return 1
    else:
        return n*factorial_1(n-1)
print("1!:", factorial_1(1))
print("2!:", factorial_1(2))
print("3!:", factorial_1(3))
print("4!:", factorial_1(4))
print("5!:", factorial_1(5))
print("6!:", factorial_1(6))