vowels='aeiou'
ip_str='You will never go wrong in doing what is right.'

ip_str=ip_str.casefold()
count={}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char]+=1
        
print(count)

ip_str='The secret of passion is purpose.'
ip_str=ip_str.casefold()

count={x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)