
import math
def some_operation(arr):
    ans = 0.0
    log2=math.log(2)
    for n in range(arr[0],arr[1]):
        ans+=(1 + n*log2)/math.log(n)
    return round(ans,arr[2])

T=int(input())

for _ in range(0,T):
    print(some_operation([int(i) for i in input().split()][:3]))



# Minimised code
from math import log
def s(x):
    a = 0
    b=log(2)
    for n in range(x[0],x[1]):
        a+=(1 + n*b)/log(n)
    return round(a,x[2])
for _ in range(0,int(input())):
    print(s([int(i) for i in input().split()][:3]))
