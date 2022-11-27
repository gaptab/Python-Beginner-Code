terms=int(input("How many terms? "))

result=list(map(lambda x:2**x, range(terms)))

print("The total number of terms are:",terms)

for i in range(terms):
    print("Value of 2 to power",i,'is:',result[i])