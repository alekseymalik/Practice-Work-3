a = int(input("First: "))
b = int(input("Second: "))
a_1 = a**2+b**2
a_2 = (a+b)**2
print(a_1,"|",a_2)
if a_1 > a_2:
    print("Сумма квадратів більше ніж квадрат суми.")
elif a_1 == a_2:
    print("Однакові")
elif a_1 < a_2:
    print("Квадрат суми більше ніж сумма квадратів.")