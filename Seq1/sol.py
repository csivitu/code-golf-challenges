
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

