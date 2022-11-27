random_string='   this is good.'
print(random_string.lstrip())
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website='https://www.wikipedia.com/'
print(website.lstrip('htps:/.'))

s1=' I love Python Tutorial '
print(s1.lstrip())
s2='###HelloWorld###'
print(s2.lstrip('#'))
#rstrip

random_string='this is good    '
print(random_string.rstrip())

print(random_string.rstrip('si oo'))

print(random_string.rstrip('sid oo'))

website='www.wikipedia.com/'
print(website.rstrip('m/.'))

s1=' I Love Python Tutorials '
print(s1.rstrip())

s2='###HelloWorld###'
print(s2.rstrip('#'))














