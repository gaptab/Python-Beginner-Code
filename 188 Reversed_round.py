seq_string='Python'
print(list(reversed(seq_string)))

seq_tuple=('P','y','t','h','o','n')
print(list(reversed(seq_tuple)))

seq_range=range(5,9)
print(list(reversed(seq_range)))

seq_list=[1,2,4,6,3]
print(list(reversed(seq_list)))

class Vowels:
    vowels=['a','e','i','o','u']
    
    def __reversed__(self):
        return reversed(self.vowels)
    
v=Vowels()
print(list(reversed(v)))
#round()

print(round(10))

print(round(10.7))

print(round(5.5))


print(round(2.665,2))
print(round(2.675,2))
















