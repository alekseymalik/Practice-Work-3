import math
a = int(input("First: "))
b = int(input("Second: "))
func_1 = (a**2)-(b**2)
func_2 = math.fabs((a-b)**2)
if func_1 > func_2:
    print("Різниця квадратів більше.")
elif func_1 < func_2:
    print("Модуль квадрата різниці більше.")
elif func_1 == func_2:
    print("Вони однакові.")
