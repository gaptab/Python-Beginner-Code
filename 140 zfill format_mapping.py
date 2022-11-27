text='program is fun'
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))

number='-690'
print(number.zfill(8))
number='+690'
print(number.zfill(8))
text='--random_text'
print(text.zfill(20))
#map()
point={'x':9,'y':-6}
print('{x}{y}'.format(**point))

point={'x':9,'y':-6,'z':0}
print('{x}{y}{z}'.format(**point))

#dict subclass
class Coordinate(dict):
    def __missing__(self,key):
        return key


print('({x}, {y})'.format_map(Coordinate(x='9')))
print('({x}, {y})'.format_map(Coordinate(x='5')))
print('({x}, {y})'.format_map(Coordinate(x='9',y='6')))
















