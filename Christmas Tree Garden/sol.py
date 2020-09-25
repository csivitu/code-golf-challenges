r=int(input())
c=int(input())
a=int(input())
b=int(input())

odd=0
if c%2!=0:
    odd=1 
for p in range(0,r):
    for i in range (0,b):
        for j in range (0,int(c/2)):
            if(i+1<=b-a):
                for k in range (0,(a*2)):
                    print(end =" ")
            else:
                for k in range(0,-1-i+b):
                    print(end = " ")
                for k in range(0,2*(i-(b-a))+1):
                    print("*", end = "")
                for k in range(0,-i+b):
                    print(end = " ")
            for k in range(0,b-i-1):
                print(end = " ")
            for k in range(0,(2*i)+1):
                print("*", end = "")
            for k in range(0,b-i):
                print(end = " ")
        if(odd==1 and i+1>b-a):
                for k in range(0,-1-i+b):
                    print(end = " ")
                for k in range(0,2*(i-(b-a))+1):
                    print("*", end = "")
                for k in range(0,-i+b):
                    print(end = " ")
        print("\r")
    for i in range(1,c+1):
        if(i%2!=0):
            for k in range(0,a-1):
                print(end = " ")
            print('*', end='')
            for k in range(0,a-1):
                print(end = " ")
        else:
            for k in range(0,b-1):
                print(end = " ")
            print('*',end = '')
            for k in range(0,b-1):
                print(end = " ")
        print(end = ' ')
    print("\r")
    print("\r")