
def simpleGenerator(numbers):
    i=0
    while True:
        check=input("Do you want to generate a number? if yes press y else press n:")
        if check in ('Y','y') and len(numbers)>1:
            yield numbers[i]
            i+=1
        else:
            print("Bye!")
            break
        
for number in simpleGenerator([10,11,12,13,14]):
    print(number)