random_byte_array=bytearray('ABC','utf-8')
mv=memoryview(random_byte_array)
print(mv[0])

print(bytes(mv[0:2]))

print(list(mv[0:3]))

random_byte_array=bytearray('ABC','utf-8')
print(random_byte_array)
mv=memoryview((random_byte_array))

mv[1]=90
print(random_byte_array)

#next()
random=[5,6,'Python']
random_iterator=iter(random)
print(random_iterator)

print(next(random_iterator))


print(next(random_iterator))

print(next(random_iterator))

random=[5,9]
random_iterator=iter(random)
print(next(random_iterator,'-1'))

print(next(random_iterator,'-1'))

print(next(random_iterator,'-1'))
print(next(random_iterator,'-1'))





