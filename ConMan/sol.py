'''
Let A be an integer from input. You have to perform one such operation on A to convert it into B (also an integer) such that
B - (any one digit of B) = A
'''
def some_operation(A):
    # do some stff here

T=int(input())
A=int(input())
for _ in range(0,T):
    print(some_operation(int(input())))

