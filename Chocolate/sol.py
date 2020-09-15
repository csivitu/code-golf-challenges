#just one solution in any of the languages we are providing needed

#should run over all test files in under 30 sec
#try that is runs even faster than 30 sec so we can allow more creative
#solutions that have shorter length but take more time

#just one solution needed(not necessarily with optimised speed or length) but 
#as an example i will provide both normal and short length(code golf) solution

'''
Normal solution
t=int(input())
for i in range(t):
	n=int(input())
	count=0
	while(n>0):
		if(n%2==1):
			count+=1
		n=n//2
	print(count)
'''

#Below provided is the code golf solution

for i in range(int(input())):
	print(bin(int(input())).count('1'))