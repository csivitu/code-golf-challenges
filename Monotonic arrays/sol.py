def isMonotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))  
for i in range(int(input())):
    A = [int(j) for j in input().split()]
    if isMonotonic(A):
        print('true')
    else:
        print('false')