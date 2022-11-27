string='Tolerance is not a easy quality'
print(string.replace('Tolerance','Acceptance'))

song='Let it be, let it be, let it be'
print(song.replace('let',"don't let",2))

string='Tolerance is not a easy quality'
print(string.replace('o','e'))
song='Let it be, let it be, let it be'
print(song.replace('let','so',1))

s1='I love Python Tutorials, I love coding'
print(s1.replace('Love','Like'))
print(s1.replace('I','He'))
#rfind

quote='Let it be, let it be, let it be'

result=quote.rfind('let it')
print(result)

result=quote.rfind('small')
print(result)

result=quote.rfind('be,')
if(result!=-1):
    print(result)
else:
    print("Doesn't contain substring")











