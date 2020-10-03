n  = int(input())
f2=0
f3=0
while(n%2==0):
    n=n//2
    f2+=1
while(n%3==0):
    n/=3
    f3+=1
if (n==1 and f2<=f3):
    print("It is possible")
    print((2*f3)-f2)
else:
    print("Impossible")