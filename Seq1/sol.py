import math
ans=0
seq=[0 for _ in range(10**5 + 1)]
log2=math.log(2)

ans=0
for i in range(2,10**5 +1):
	ans+=(1+i*log2)/math.log(i)
	seq[i]=ans
for _ in range(int(input())):
    l=[int(i) for i in input().split()][:3]
    ans=seq[l[1]]-seq[l[0]-1]
    print(ans)
    temp=str(ans)
    temp=temp+'0'*10
    pos = temp.find('.')
    print(temp[:pos+l[2]+1])
