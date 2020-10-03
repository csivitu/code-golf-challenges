from math import floor,ceil,sqrt

def check(a,b):
	b=str(b)
	for i in b:
		if(int(b)-int(i)==a):
			return True
	return False

t=int(input())
for _ in range(t):
	s=set()
	n=int(input())
	s.add(n)
	for i in range(n+1,n+10):
		if(check(n,i)):
			s.add(i)
			for j in range(i+1,i+10):
				if(check(i,j)):
					s.add(j)
					for k in range(j+1,j+10):
						if(check(j,k)):
							s.add(k)
	ans=pow(10,9)
	for i in s:
		t1=floor(sqrt(i))
		t2=ceil(sqrt(i))
		ans=min(ans,abs(i-t1*t1))
		ans=min(ans,abs(i-t2*t2))
	print(ans)
