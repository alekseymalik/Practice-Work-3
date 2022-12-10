a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))
if a==b:
    print("Треугольник равнобедренный")
elif a==c:
    print("Треугольник равнобедренный")
elif c==b:
    print("Треугольник равнобедренный")
else:
    print("Он не равнобедренный")