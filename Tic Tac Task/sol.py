def task(mint, tic, tac): 
	 
	if (tac % tic) != 0: 
		 
		if mint == 1: 
			return 0 
		elif (mint % tac) != 0: 
			return -1
		else: 
			return int(mint / tac) 
	 
	c = tac / tic 
	x = 0
	y = 0
	 
	while (mint % tac == 0): 
		mint /= tac  
		x += 1
 
	while (mint % c == 0): 
		mint /= c  
		y += 1
	 
	if mint == 1:  
		min_steps = x + 2 * y  
		return min_steps 
	else: 
		return -1

k =  int(input())
while(k>0):
	k=k-1
	mint = int(input())
	tic = int(input())
	tac = int(input())
	print(task(mint, tic, tac)) 
 
