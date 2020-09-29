def seat(arr):
    arr1=[]
    arr2=[]
    arr3={}
    for i in range(0,len(arr)):
        b=0
        for a in range (0,len(arr2)):
            if arr2[a]==0 :
                b=1
                index = a
                break
        if(b==0):
            arr2.append(0)
            index = len(arr2)-1
            for l in range (0,5):
                arr1.append(0)
            arr3[index]=[]
        for e in range (index*5,(index*5)+5):
            if(arr1[e]==0):
                arr1[e]=arr[i]
                arr3[index].append(arr[i])
                break
        check=0
        for c in range (index*5,(index*5)+5):
            if(arr1[c]==0):
                check =1
                break
        if(check==0):
            arr2[index]=1
        for k in range (0,len(arr2)):
            for c in range(k*5, (k*5)+5):
                if(arr1[c]!=0 and c!=e):
                    arr1[c]= arr1[c]-1
            if(arr2[k]==1):
                w=(arr1[k*5])
                index1=k*5
                for c in range(k*5, (k*5)+5):
                    if(arr1[c]>w):
                       w=arr1[c]
                       index1=c
                if(arr1[index1]==0):
                   arr2[k]=0
    print(len(arr2))
    for i in range(0,len(arr2)):
        print(arr3[i])
arr = [] 
n = int(input()) 
for i in range(0, n): 
    e = int(input()) 
    arr.append(e)
seat(arr)