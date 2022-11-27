
def decorator(myFunc):
    def insideDecorator(*args):
        print('insideDecorator function executed before {}'.format(myFunc.__name__))
        return myFunc(*args)
    return insideDecorator

@decorator 
def display(*args):
    print('In display function')
    print(*args)
    
display('Hi','How are you?',881212)