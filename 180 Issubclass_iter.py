class Polygon:
    def __init__(polygonType):
        print("Polygon is a ",polygonType)
        
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')
        
print(issubclass(Triangle,Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle,(list,Polygon)))
print(issubclass(Polygon, (list,Polygon)))

#iter()
vowels=['a','e','i','o','u']
vowels_iter=iter(vowels)

print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))

class PrintNumber:
    def __init__(self,max):
        self.max=max
        
    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        if(self.num>=self.max):
            raise StopIteration
        self.num+=1
        return self.num
print_num=PrintNumber(3)

print_num_iter=iter(print_num)
print(next(print_num_iter))
print(next(print_num_iter))
print(next(print_num_iter))
class DoubleIt:
    def __init__(self):
        self.start=1
    def __iter__(self):
        return self
    def __next__(self):
        self.start *=2
        return self.start
    
    __call__=__next__

my_iter=iter(DoubleIt(),16)

for x in my_iter:
    print(x)


































