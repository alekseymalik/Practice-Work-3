#Скласти програму, яка здійснює переклад величин з радіанної заходи в градусну або навпаки. Програма повинна запитувати, який переклад потрібно здійснити, і виконувати вказану дію.
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
list = []
def pos_num(a,b,c,list):
    if a >= 0:
        list.append(a)
    if b >= 0:
        list.append(b)
    if c >= 0:
        list.append(c)
    print(f"{len(list)} positive numbers in list")
pos_num(a,b,c,list)