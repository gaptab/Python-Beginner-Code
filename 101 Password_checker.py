import time
pwd='FreeTimeisNotaLuxury'
def IInd_func():
    count1=0
    for j in range(5):
        a=0
        count=0
        user_pwd=input('Enter the password:')
        for i in range (len(pwd)):
            if user_pwd[i]==pwd[a]:
                a+=1
                count+=1
        if count==len(pwd):
            print("Correct password!!")
            break
        else:
            count1+=1
            print("Incorrect password!!")
            
        if count==5:
            time.sleep(30)
            IInd_func()
IInd_func()