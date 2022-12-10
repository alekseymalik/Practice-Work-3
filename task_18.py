a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
list_pos = []
list_neg = []
def func(a,b,c):
    if a >= 0:
        a = a**2
        list_pos.append(a)
    else:
        list_neg.append(a)
    if b >= 0:
        b = b**2
        list_pos.append(b)
    else:
        list_neg.append(b)
    if c >= 0:
        c = c**2
        list_pos.append(c)
    else:
        list_neg.append(c)
    print(f"Список позитивных чисел: {list_pos}")
    print(f"Список негативных чисел: {list_neg}")
func(a,b,c)