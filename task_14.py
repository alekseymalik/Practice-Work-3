import math
a = 2
b = 2
c = 2
P = a+b+c
S = math.sqrt(P*(P-a)*(P-b)*(P-c))
if a + b > c and a + c > b and b + c > a:
    print(f"Площа: {S} см2")
else:
    print("Трикутника не існує")