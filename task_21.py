import math
#проверку можно совершить через теорему пифагора.
x = int(input("Гипотенуза: ")) #гипотенуза 8
y = int(input("Катет a: "))#катет a 2
z = int(input("Катет b: ")) #катет b 2
pifagor_1 = y**2 + z**2
pifagor = round(math.sqrt(x**2))
if pifagor_1 == pifagor:
    print(f"Це прямокутний трикутник!")
else:
    print("Не існує")