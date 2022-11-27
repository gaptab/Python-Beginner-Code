vowel_string='aeiou'
print(list(vowel_string))

vowel_tuple=('a','e','i','o','u')
print(list(vowel_tuple))
vowel_list=['a','e','i','o','u']
print(list(vowel_list))

vowel_set={'a','e','i','o','u'}
print(list(vowel_set))

vowel_dictionary={'a':1,'e':2,'i':3,'o':4,'u':5}
print(list(vowel_dictionary))

class PowTwo:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.num=0
        return self
    
    def __next__(self):
        if (self.num>=self.max):
            raise StopIteration
        result=2**self.num
        self.num+=1
        return result

pow_two=PowTwo(5)
pow_two_iter=iter(pow_two)
print(list(pow_two_iter))
#locals()
def localsNotPresent():
    return locals()

def localsPresent():
    present=True
    return locals()

print(localsNotPresent())
print(localsPresent())


def localsPresent():
    present=True
    print(present)
    locals()['present']=False
    print(present)

localsPresent()















