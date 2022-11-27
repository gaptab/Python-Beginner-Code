a=0b1010
b=100
c=0o310
d=0x12c

int_1=10
int_2=77

float_1=1.34
float_2=1.5e2

x=3.14j

print(a,b,c,d)
print(int_1,int_2)
print(float_1,float_2)
print(x,x.imag,x.real)

a='''apple'''
b="""apple"""
c='apple'
d="apple"

print(a,b,c,d)


strings="This is python"
char="C"
multiline_str=""" This is multiline string"""
unicode=U"\u00dcnic\u00f6de"
raw_str=r"raw \n string"
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#boolean literals

x=(1==True)
y=(1==False)
a=True+6
print(a)
b=False+90
print(b)


#special literals

juice="Available"
soup=None 
def menu(x):
    if x==juice:
        print(juice)
    else:
        print(soup)
menu(juice)
menu(soup)
fruits1={'Banana','Apple','Strawberry'}
fruits2=('Banana','Apple','Strawberry')
fruits3=['Banana','Apple','Strawberry']
fruits4={1:'Banana',2:'Apple',3:'Strawberry'}

print(fruits4)




























