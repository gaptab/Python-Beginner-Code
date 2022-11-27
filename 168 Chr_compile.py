print(chr(97))
print(chr(65))
print(chr(1200))

print(chr(-1))

#compile()

codeInString='a=5\nb=6\nsum=a+b\nprint("sum=",sum)'
codeObject=compile(codeInString,'sumString','exec')
exec(codeObject)
