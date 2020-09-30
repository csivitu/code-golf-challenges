def s(x,i):
	o=0
	e=0
	for j in range(len(x)):
		if(j%2):
			e+=int(x[j])
		else:
			o+=int(x[j])
	return o if i%2 else e

for i in range(int(input())):
    print(s(input(),i+1))
