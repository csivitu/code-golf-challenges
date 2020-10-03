i=int(input())
a=[]
while(i>0):
    n=int(input())
    p=((n**2)+n+2)//2
    a.append(p)
    i-=1
for i in a:
    print(i)
