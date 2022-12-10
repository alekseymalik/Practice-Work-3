import math
radian = int(input("Radian: "))
degree = radian*180/math.pi
if math.cos(degree) > math.sin(degree):
    print("Косинус больше чем синус")
elif math.sin(degree) > math.cos(degree):
    print("Синус больше чем косинус")
elif math.sin(degree) == math.cos(degree):
    print("Они одинаковы")