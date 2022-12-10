import math
print("Если что, все результаты округлены.")
choose_func = int(input("""
1. Radians -> Degree
2. Degree -> Radians
: """))

def r_degrees(d):
    r = d * math.pi/180
    print(f"Ответ: {round(r)}°")
def d_radian(r):
    d = r * math.pi/180
    print(f"Ответ: {round(d)}")
if choose_func == 1:
    choose_r = int(input("Radians: "))
    r_degrees(choose_r)
if choose_func == 2:
    choose_d = int(input("Degree: "))
    d_radian(choose_d)