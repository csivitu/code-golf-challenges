mod=pow(10,9)+7

def fibonacci(n): 
    a = 0
    b = 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = (a + b)%mod
            a = b 
            b = c 
        return b 
  
t=int(input())
for _ in range(t):
	n=int(input())
	print(fibonacci(n+1)) 