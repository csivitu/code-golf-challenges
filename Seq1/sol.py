# Big Code

import math
def some_operation(arr):
    ans = 0
    log2=math.log(2)


    for n in range(arr[0],arr[1]+1):
        i=(1 + n*log2)/math.log(n)
        ans+=i
        print(i)
    print()
    return round(ans,arr[2])

T=int(input())

for _ in range(0,T):
    print(some_operation([int(i) for i in input().split()][:3]))


T=int(input())


## Shorter code

import math
ans=0
seq=[0 for _ in range(10**5 + 1)]
log2=math.log(2)

for i in range(2,10**5 +1):
	ans+=(1+i*log2)/math.log(i)
	seq[i]=ans
for _ in range(int(input())):
    l=[int(i) for i in input().split()][:3]
    ans=seq[l[1]]-seq[l[0]-1]
    print('{:.{prec}f}'.format(ans, prec=l[2]))
