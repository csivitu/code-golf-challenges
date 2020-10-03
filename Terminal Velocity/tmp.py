import random

n = random.randint(1, 100000)

print(n)

for i in range(n):
    c = random.randint(400, 4000)
    d = random.randint(50, 150)
    k1 = random.uniform(0, 0.1)
    k2 = random.uniform(0, 1)
    print(c, d, round(k1, 2), round(k2, 1))