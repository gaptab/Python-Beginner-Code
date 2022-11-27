z=complex(2,-3)
print(z)
z=complex(1)
print(z)
z=complex()
print(z)
z=complex('5-9j')
print(z)

a=2+3j
print(a)
print(type(a))

b=-2j
print(b)
print(type(b))

x=0j
print(x)
print(type(x))
#delattr()

class Coordinate:
    x=10
    y=-5
    z=0
point1=Coordinate()
print(point1.x)
print(point1.y)
print(point1.z)
#delattr(Coordinate,'z')


point1=Coordinate()
print(point1.x)
print(point1.y)
print(point1.z)
del Coordinate.z
print(point1.z)











