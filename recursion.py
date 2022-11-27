def factorial(n):
    if n==1:
        return 1
    else:
        return (n * factorial(n-1))
    
num=6
#6x5x4x3x2x1=720

print("The factorial of",num,"is",factorial(num))