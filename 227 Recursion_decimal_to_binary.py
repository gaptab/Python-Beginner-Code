def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n%2,end='')
    
dec=100

convertToBinary(dec)
print(' is a binary equivalent to decimal of',dec)