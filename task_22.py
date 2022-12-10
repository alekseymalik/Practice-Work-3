import math

side_square = int(input("Side square: "))
radius = int(input("Radius circle: "))
s_square = side_square**2
s_circle = math.pi*radius**2
if s_circle > s_square:
    print("Площадь круга больше чем площадь квадрата.")
elif s_circle < s_square:
    print("Площадь квадрата больше чем площадь круга.")
elif s_circle == s_square:
    print("Они одинаковы.")