#Default argument

def greet(name,msg='Good morning!'):
    print("Hello", name +', '+msg)
    
greet("Bhism")
greet("Duryodhan","How do you do?")
greet("Karna","Good night!")

#Keyword argument
def add_two_numbers(num1,num2):
    total=num1+num2
    return total
print(add_two_numbers(num2=70, num1=43))


#Arbitrary argument

def greet(*names):
    for name in names:
        print("Hello",name)
        
greet("Yudhistir","Arjun","Bheem","Nakul","Sahadev")

def addition(*numbers):
    total=0
    for number in numbers:
        total=total+number 
    print("Sum is:",total)
    
addition()
addition(12,56,78)
addition(1,24,67,34,50.11)