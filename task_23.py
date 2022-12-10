
list_pos = []
list_neg = []
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
if a >=0:
    a = a**3
    list_pos.append(a)
if a < 0:
    a = a*0
    list_neg.append(a)
if b >=0:
    b = b**3
    list_pos.append(b)
if b < 0:
    b = b*0
    list_neg.append(b)
if c >=0:
    c = c**3
    list_pos.append(c)
if c < 0:
    c = c*0
    list_neg.append(c)
print(f"Позитивные числа: {list_pos}")
print(f"Негативные числа: {list_neg}")