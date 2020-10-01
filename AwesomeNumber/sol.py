def sumDigitSquare(n) : 
    sq = 0
    while (n) : 
        digit = n % 10
        sq = sq + digit * digit 
        n = n // 10
    return sq
def isAwsome(n) : 
    while (1) :
        if (n == 1) : 
            return True 
        n = sumDigitSquare(n) 
        if (n == 4) : 
            return False
    return False
for i in range(int(input())):
    if (isAwsome(int(input()))):
        print("Awsome")
    else:
        print("Not Awsome")