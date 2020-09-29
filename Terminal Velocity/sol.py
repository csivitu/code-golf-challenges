"""
You are working on building the world's fastest car. Your mission is to find out the maximum speed you can reach given the weight of the car, the weight of the driver, and the loss in velocity due to drag.

Assume the following:
c is the weight of the car.
d is the weight of the driver.
u is the maximum speed you can reach without experiencing drag.
v is the decrease in velocity experience due to drag.

u = k1 * 67108864 / (c + d)
v = k2 * u

c d k1 k2
"""

def test_solution():
    c, d, k1, k2 = list(map(float, input().split()))
    u = k1 * 67108864 / (c + d)
    v = k2 * u
    print(int(u - v))

# Of course, there might be something better than this. This is of length 68.
def codegolf_solution():
    a,b,c,d=map(float,input().split());print(int((2<<25)*(1-d)*c/(a+b)))

codegolf_solution()
