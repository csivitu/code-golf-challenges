a = input().replace(' ','')
a = ''.join(e for e in a if e.isalpha())
print(a)
b =[]
c=1
d=0
e = ''
t = a
for h in range (len(a)):
    for i in range (len(t)):
        e=''
        for j in range (len(t)-i):
            e += t[j]
        d=0;
        for k in e:
            if (k != 'a' and k != 'z'):
                if(chr(ord(k)+1) not in e and chr(ord(k)-1) not in e):
                    d=1
                    break
            elif (k == 'a'):
                if ( 'z' not in e and 'b' not in e):
                    d=1
                    break
            elif (k == 'z'):
                if ('a' not in e and 'y' not in e):
                    d=1
                    break
        if(d==0):
            r=''
            for q in e:
                if (q not in r):
                    r += q
            if len(r)>c:
                c=len(r)
    t = a[h+1:len(a)]
if(a==''):
    print('0')
else:
    print(c)