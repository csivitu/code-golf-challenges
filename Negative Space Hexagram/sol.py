a = int(input())
print('*'*(a*2+1))
b = int(a/2)
c = 1
for i in range (b-1):
    print('*'*(int(((a-1)*2+1)/2)-i+1), end='')
    print(' '*(i*2+1), end='')
    print('*'*(int(((a-1)*2+1)/2)-i+1))
if(a%4 == 0):
    c=0
for k in range (int(a/4) + c):
    print('*'*(k+1), end ='')
    print(' '*((a-1)*2+1-k*2), end ='')
    print('*'*(k+1))
for h in range (i+k+2,a):
    print('*'*(int(((a-1)*2+1)/2)-h+1), end='')
    print(' '*(h*2+1), end='')
    print('*'*(int(((a-1)*2+1)/2)-h+1))
for i in range (b-1):
    print('*'*(int(((a-1)*2+1)/2)-b+3+i), end='')
    print(' '*((b-2-i)*2+1), end='')
    print('*'*(int((((a-1)*2)+1)/2)-b+3+i))
print('*'*(a*2+1))