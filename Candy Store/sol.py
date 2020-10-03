def hcf(p, q): 
	if (q == 0): 
		return p 
	return hcf(q, p % q) 
	
 
def func(S, p, q): 
	g = hcf(p, q) 
	if (S % g == 0): 
		return 1
	else: 
		return 0

k = int(input())
while(k>0):
	k=k-1
	S = int(input())
	p = int(input())
	q = int(input())
	print(func(S,p,q))
