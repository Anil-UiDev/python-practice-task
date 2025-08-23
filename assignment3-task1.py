def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
        
num = input("Enter a Number : ")

result = factorial(int(num))
print(f"Factorial of {num} is: {result}")
