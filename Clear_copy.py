d={1:'one',2:'two'}
d.clear()
print(d)

#copy()

original={1:'one',2:'two'}
new=original.copy()
print(original)
print(new)

# = operator
new=original
new.clear()
print(new)
print(original)

original={1:'one',2:'two'}
new=original.copy()
new.clear()
print(new)
print(original)