
def s(x,i):
    a=0
    b=0
    c=0
    while(x):
        if(c%2):
            a+=x%10
        else:
            b+=x%10
       
        x//=10
        c+=1
    return a if i%2 else b

for i in range(int(input())):
    print(s(int(input()),i))
