square_dict=dict()
for num in range(1,11):
    square_dict[num]=num*num
print(square_dict)

square_dict={num:num*num for num in range(1,21)}
print(square_dict)

old_price={'milk':2.03,'bread':2.6,'butter':2.6}
dollar_to_pound=0.76
new_price={item:value*dollar_to_pound for (item,value)in old_price.items()}
print(new_price)

#conditionals
original_dict={'Duryodhan':36,'Drona':48,'Kripa':57,'Karna':33}

even_dict={k:v for (k,v)in original_dict.items() if v%2==0}
print(even_dict)

#multiple if
new_dict={k:v for (k,v) in original_dict.items() if v%2!=0 if v<40}
print(new_dict)

#if-else

new_dict1={k: ('old' if v>40 else 'young')
    for(k,v)in original_dict.items()}
print(new_dict1)

#nested
nes_dict={'dict1':{'color':'red','shape':'square'},'dict2':{'color':'pink','shape':'round'}}
print(nes_dict)

dictionary={k1:{k2: K1*k2 for k2 in range(1,6)} for k1 inranf=ge}











