#items()

dt={"a":"believe","b":"you can","c":"halfway there"}
for key, value in dt.items():
    print(key,value)
    
dt={"a":"believe","b":"you can","c":"halfway there"}

for key in dt:
    print(key,dt[key])
    
# return keys or values explicitly

dt={"a":"believe","b":"you can","c":"halfway there"}

for key in dt.keys():
    print(key)
for value in dt.values():
    print(value)