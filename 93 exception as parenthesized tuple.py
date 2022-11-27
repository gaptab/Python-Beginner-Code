string=input("Enter a string and a number:")
try:
    num=int(input())
    print(string+num)
except(TypeError,ValueError) as e:
    print(e)